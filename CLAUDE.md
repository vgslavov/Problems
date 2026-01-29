# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a comprehensive interview preparation and problem-solving repository containing:
- Algorithm and data structure implementations
- LeetCode solutions (218 Python files)
- System design documentation and implementations
- Design patterns in C++
- Template collections for competitive programming

## Development Commands

### C++ Design Problems
```bash
# Navigate to design directory
cd design

# Build all C++ executables using CMake
mkdir -p build && cd build
cmake ..
make

# Build specific executable
make vector        # Build vector implementation
make queue         # Build queue implementation
make orderbook     # Build order book system
make shared_ptr    # Build smart pointer examples

# Run executables
./vector
./queue
./orderbook

# Build and run tests
cd tests
cmake .
make
# Run individual test files (*.t.cpp)
```

### Python Solutions
```bash
# Run individual Python solutions
python3 leetcode/[problem_name].py
python3 design/queue.py
python3 algomonster/[algorithm].py

# Execute template file with examples
./templates.py
```

## Code Architecture

### Directory Structure
- **`leetcode/`** - LeetCode problem solutions (218 Python files)
- **`design/`** - System design implementations and C++ fundamentals
  - C++ implementations: smart pointers, RAII patterns, order book
  - Python implementations: queue, event manager
  - `tests/` - CMake-based C++ test framework
- **`algomonster/`** - Algorithm implementations from Algo Monster
- **`patterns/`** - Design pattern implementations in C++
- **`archive/`** - Historical solutions from various platforms
- **`threads/`** - Concurrency examples

### Key Template Files
- **`templates.py`** - Comprehensive Python algorithm templates (two pointers, sliding window, BFS/DFS, etc.)
- **`templates.cpp`** - C++ class templates and STL usage patterns
- **`cheatsheets.md`** - Algorithm complexity references and patterns
- **`sysdesign.md`** - System design concepts and patterns
- **`lld.md`** - Low-level design patterns and implementations

### C++ Build System
- Uses CMake with C++17 standard
- Each `.cpp` file in `design/` becomes a standalone executable
- Test files follow `*.t.cpp` naming convention
- VSCode configured with extensive C++ IntelliSense support

### Code Conventions
- **Python**: Executable templates with shebang `#!/usr/bin/env python3`
- **C++**: Namespace `notstd` for custom implementations
- Problem solutions include complexity analysis and constraints in comments
- Design implementations focus on interview-relevant patterns (RAII, Rule of 3/5/0)