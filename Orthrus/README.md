# Orthrus: A Framework to Analyze Solidity Smart Contracts

Orthrus is an execution framework aimed at simplifying the execution of analysis tools on smart contracts.


## Features

- A plugin system to easily add new analysis tools, based on Docker images;

- Parallel execution of the tools to speed up the execution time;

- An output mechanism that normalizes the way the tools are outputting the results, and simplifies the process of the output across tools.

- Automatic detection and download of the correct version of the Solidity compiler as required by the contract under analysis.

## Supported Tools

1. Mythril
2. Slither

## Requirements

- Unix-based system
- [Docker](https://docs.docker.com/install)
- [Python3](https://www.python.org)


## License
The license in the file `LICENSE` applies to all the files in this repository,
except for all the smart contracts in the `dataset` folder. 
The smart contracts in this folder are
publicly available, were obtained using the Etherscan APIs, and retain their
original licenses. Please contact us for any additional questions.
