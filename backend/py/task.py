from dataclasses import dataclass

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    # first get parents
    parents = set(file.parent for file in files)

    # then include every file that's not a parent
    return [file.name for file in files if file.id not in parents]


"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    # get category to file mapping
    categories = {}
    for file in files:
        for category in file.categories:
            if category not in categories:
                categories[category] = 0
            else:
                categories[category] += 1

    # sort categories by descending size and ascneding alpha
    return sorted(
        categories.keys(), key=lambda category : (-categories[category], category)
    )[:k]


"""
Task 3
"""
def largestFileSize(files: list[File]) -> int:
    # guard check
    if len(files) == 0:
        return 0

    @dataclass
    class FileNode:
        def __init__(self, size: int):
            self.size = size
            self.children = []

    # recursively gets size of file
    def fileSize(file: int):
        return fileTree[file].size + sum(map(fileSize, fileTree[file].children))

    # create tree storing file children and file size
    fileTree = {-1: FileNode(0)}
    for file in files:
        fileTree[file.id] = FileNode(file.size)
    for file in files:
        fileTree[file.parent].children.append(file.id)
    
    return max(map(fileSize, fileTree[-1].children))


if __name__ == '__main__':
    testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
    ]

    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]

    assert kLargestCategories(testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992
