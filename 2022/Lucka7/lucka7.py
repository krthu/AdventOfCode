# @dataclass(frozen=True)
class File:
    name: str
    size: int

class Directory:
    def __init__(self, name: str) -> None:
        self._name = name
        self._files: list[File] = []     # files in this dir
        self._dirs: list[Directory] = [] # directories in this dir

        def name(self):
            return self._name
        
        def add_file(self, a_file: File):
            self._files.append(a_file)

        def add_directory(self, a_dir: Directory):
            self._dirs.append(a_dir)
            a_dir.parent_dir = self  



# storage = []

# for line in f:
#     charArr = line.split()
#     if charArr[0] == "$":
#         if charArr[1] == "cd":
#             if charArr[2] == "..":
#                 print("..")
#             else:
    

            
   
# print(storage)    
def day7(s, part2=False):
  stack, sizes = [], []
  for line in s.splitlines():
    if line == '$ cd ..':
      size = stack.pop()
      sizes.append(size)
      stack[-1] += size
    elif line.startswith('$ cd '):
      stack.append(0)
    elif line[0].isdigit():
      stack[-1] += int(line.split()[0])
  sizes.extend(itertools.accumulate(stack[::-1]))
  return (sum(s for s in sizes if s <= 100_000) if not part2 else
          min(s for s in sizes if s >= max(sizes) - 40_000_000))


s = open("/Users/kristianthun/Documents/Code/AdventOfCode2022/Lucka7/sample.txt", "r")
text = day7(s)