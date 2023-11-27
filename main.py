import os
from inputs import repo_path, output_path

def read_files(directory, excluded_folders, excluded_files_and_extensions):
    all_text = ""
    for root, dirs, files in os.walk(directory, topdown=True):
        # Ignore specified folders
        dirs[:] = [d for d in dirs if not any(ex_dir in os.path.join(root, d) for ex_dir in excluded_folders)]

        for file in files:
            if any(ex_file in file or file.endswith(ex_file) for ex_file in excluded_files_and_extensions):
                continue  # Ignore specified files

            file_path = os.path.join(root, file)
            all_text += f"\n\n-----\nFile: {file_path}\n-----\n\n"
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                all_text += file.read()
                all_text += "\n\n"  # Add Space between files
    return all_text

def main():

    # Folders and files to exclude
    excluded_folders = ['.next', 'node_modules', '.git', 'dist', 'build', '.cache', 'npm-cache']
    excluded_files_and_extensions = ['package-lock.json', 'yarn.lock', '.gitignore', '.env', '.env.local', '.env.development', '.env.production', '.DS_Store', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.bmp', '.tiff', '.woff', '.woff2', '.ttf', '.otf', '.mp3', '.wav', '.mp4', '.avi', '.mov', '.flv', '.zip', '.tar', '.rar', '.gz', '.pdf', '.docx', '.xlsx', '.exe', '.sh', '.bat']

    # Read all files except specified
    concatenated_text = read_files(repo_path, excluded_folders, excluded_files_and_extensions)

    # Save the result in a txt file
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(concatenated_text)

if __name__ == "__main__":
    main()
