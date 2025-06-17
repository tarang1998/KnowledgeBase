from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict, Optional, Union


# Composite Pattern 
# New Node types, like special file formats can subclass this 
class FileSystemNode(ABC):

    def __init__(self,name:str):
        self.name = name
        self.created_at = datetime.now()
        self.modified_at = self.created_at

    @abstractmethod
    def is_file(self) -> bool:
        pass

    @abstractmethod
    def display(self, depth : int = 0 ) -> None:
        pass

    @abstractmethod
    def calculate_size(self) -> int:
        pass

    def update_modified(self):
        self.modified_at = datetime.now()


class File(FileSystemNode):
    def __init__(self,name:str):
        super().__init__(name)
        self.content = ""

    def is_file(self) -> bool:
        return True
    
    def write(self, data : str) -> None:
        self.content = data
        self.update_modified()

    def read(self) -> str:
        return self.content

    def calculate_size(self):
        return len(self.content)
    
    def display(self, depth : int = 0):
        indent = " " * (depth * 2 )
        print(f"{indent} {self.name} (size = {self.calculate_size()} bytes)") 

class Directory(FileSystemNode):
    def __init__(self, name:str):
        super().__init__(name)
        self.children :Dict[str, FileSystemNode]  = {}

    def is_file(self) -> bool:
        return False
    
    def add_child(self, node: FileSystemNode) -> None:
        self.children[node.name] = node
        self.update_modified()

    def get_child(self,name:str)-> FileSystemNode:
        return self.children.get(name,None)

    def remove_child(self, name: str) -> bool:
        if name is self.children:
            del self.children[name]
            self.update_modified()
            return True 
        return False
    
    def calculate_size(self):
        return sum(child.calculate_size() for child in self.children.values())
    
    def display(self, depth:int = 0) -> None:
        indent = " " * (depth * 2)
        count = len(self.children)
        size = self.calculate_size()
        print(f"{indent} {self.name} ({count} items) ({size} bytes))")
        for child in self.children.values():
            child.display(depth+1)


class FileSystem():
    def __init__(self):
        self.root = Directory("/")

    def _split_path(self, path : str) -> list:
        return [p for p in path.strip("/").split("/") if p]
    
    def create_path(self, path : str) -> bool:
        # Only allow paths under the root, and not supporting recreating of the root 
        if not path.startswith("/") or path == "/":
            return False
        
        parts = self._split_path(path)
        curr = self.root

        # Parse through every component except the last 
        for part in parts[:-1]:
            node = curr.get_child(part)
            if node is None: # Meaning the directory does not exists
                newDir = Directory(path)
                curr.add_child(newDir)
                curr = newDir
            else:
                # The node exist. Check if is a file
                if node.is_file():
                    return False
                curr = node
        last = parts[-1]
        if curr.get_child(last):
            return False # The file or directory is already present 
        if "." in last:
            curr.add_child(File(last))
        else: 
            curr.add_child(Directory(last))
        return True
    
    def get_node(self, path: str) -> Optional[FileSystemNode]:
        if path == "/":
            return self.root 
        if not path.startswith("/"):
            return None
        curr = self.root
        for path in self._split_path(path):
            node = curr.get_child(path) if isinstance(curr, Directory) else None
            if node is None:
                return None 
            curr = node
        return curr
    
    def delete_path(self, path:str)-> bool:
        if path == "/":
            return False
        if not path.startswith("/"):
            return False
        parts = self._split_path(parts)
        parent_path = "/" + "/".join(parts[:-1]) if len(parts)>1 else "/"
        node = self.get_node(parent_path)
        if not isinstance(node,Directory):
            return False
        return node.remove_child(parts[-1])
    
    def set_file_content(self, path:str,content)->bool:
        node = self.get_node(path)
        if isinstance(node, File):
            node.write(content)
            return True
        return False

    
    def get_file_content(self, path: str) -> Optional[str]:
        node = self.get_node(path)
        if isinstance(node, File):
            return node.read()
        return None

    def display(self) -> None:
        self.root.display()




if __name__ == "__main__":
    fs = FileSystem()
    # Example usage
    fs.create_path("/docs")
    fs.create_path("/docs/readme.txt")
    fs.set_file_content("/docs/readme.txt", "This is the README file.")
    fs.create_path("/src")
    fs.create_path("/src/main.py")
    fs.set_file_content("/src/main.py", "print('Hello World')")
    fs.display()

        