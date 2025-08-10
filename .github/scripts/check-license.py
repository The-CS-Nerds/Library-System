import sys
from pathlib import Path

REQUIRED_LICENSE = [
    "#",
    "#    This program is free software: you can redistribute it and/or modify",
    "#    it under the terms of the GNU Affero General Public License as published",
    "#    by the Free Software Foundation, either version 3 of the License, or",
    "#    (at your option) any later version.",
    "#",
    "#    This program is distributed in the hope that it will be useful,",
    "#    but WITHOUT ANY WARRANTY; without even the implied warranty of",
    "#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the",
    "#    GNU Affero General Public License for more details.",
    "#",
    "#    You should have received a copy of the GNU Affero General Public License",
    "#    along with this program.  If not, see <https://www.gnu.org/licenses/>."
]

SOURCE_EXTS = {".py", ".js", ".ts", ".java", ".c", ".cpp", ".go", ".rs"}

IGNORE_DIRS = {
    "docs",
    ".github"
}
IGNORE_FILES = {
    "LICENSE",
    "mkdocs.yml",
    ".readthedocs.yml",
    ".gitignore"

}

def check_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f.readlines()]
    except UnicodeDecodeError:
        return True
    if len(lines) < len(REQUIRED_LICENSE) + 2:
        return False

    return lines[2:2+len(REQUIRED_LICENSE)] == REQUIRED_LICENSE

def main():
    failed_files = []
    for file_path in Path(".").rglob("*"):
        if (
            file_path.is_file()
            and file_path.suffix in SOURCE_EXTS
            and not any(part in IGNORE_DIRS for part in file_path.parts)
            and file_path.name not in IGNORE_FILES
        ):
            if not check_file(file_path):
                failed_files.append(str(file_path))

    if failed_files:
        print("License header check failed for these files:")
        for f in failed_files:
            print(f"  - {f}")
        sys.exit(1)

if __name__ == "__main__":
    main()
