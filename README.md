# UCS & IDFS Search Algorithms

This project demonstrates the implementation of two fundamental search algorithms in Artificial Intelligence:

1. **Uniform Cost Search (UCS)**: A search algorithm that expands the least-cost node first.
2. **Iterative Deepening Depth-First Search (IDFS)**: A combination of depth-first and breadth-first search techniques.

## Features

- Implementation of UCS and IDFS algorithms.
- Example use cases and test cases for both algorithms.
- Easy-to-understand code structure for educational purposes.

## Prerequisites

- Python 3.x installed on your system.
- Basic understanding of search algorithms and graph theory.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd "UCS & IDFS"
    ```

## Usage

1. Run the UCS algorithm:
    ```bash
    python ucs.py
    ```
2. Run the IDFS algorithm:
    ```bash
    python idfs.py
    ```

## File Structure

- `ucs.py`: Implementation of the Uniform Cost Search algorithm.
- `idfs.py`: Implementation of the Iterative Deepening Depth-First Search algorithm.
- `README.md`: Documentation for the project.

## Examples

### Uniform Cost Search
Input graph:
```
A --(1)--> B --(2)--> C
```
Output:
```
Path: A -> B -> C
Cost: 3
```

### Iterative Deepening Depth-First Search
Input graph:
```
A -> B -> C
```
Output:
```
Path: A -> B -> C
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.