import os
import shutil
from pathlib import Path

# Settings
tf_directory = Path('C:/Steam/steamapps/common/Team Fortress 2/tf')
config_directory = Path('D:/TF2 Configs')

# Check currently active config
configs = [d for d in os.listdir(config_directory)
    if os.path.isdir(os.path.join(config_directory, d))]

active_path = config_directory / 'current_cfg.txt'
if not active_path.exists():
    active_path.write_text('', encoding='utf-8')

active_cfg = active_path.read_text(encoding='utf-8').strip()

# Determine new config
if active_cfg in configs:
    active_index = (configs.index(active_cfg) + 1) % len(configs)
else:
    active_index = 0
new_cfg = configs[active_index]

active_path.write_text(new_cfg, encoding='utf-8')

# Remove active config
if active_cfg:
    print(f'removing config: {active_cfg}')
    active_config_path = config_directory / active_cfg

    for directory in active_config_path.iterdir():
        if not directory.is_dir():
            print(f'skipping: {directory}')
            continue
        tf_subdir = tf_directory / directory.name

        for root, dirs , files in os.walk(directory):
            root = Path(root)
            relative_path = root.relative_to(directory)
            tf_target_path = tf_subdir / relative_path

            for file in files:
                tf_file_path = tf_target_path / file
                try:
                    tf_file_path.unlink()
                except FileNotFoundError:
                    print(f'File not found: {tf_file_path}')

custom_dir = tf_directory / 'custom'
for file in custom_dir.iterdir():
    if file.suffix == '.cache':
        try:
            file.unlink()
        except FileNotFoundError:
            print(f'File not found: {file}')

# Copy new config
print(f'Copying config: {new_cfg}')

new_config_path = config_directory / new_cfg
shutil.copytree(new_config_path, tf_directory, dirs_exist_ok=True)
