# SaladCat
**A distributed hashcat implementation using Salad Cloud and Hashtopolis**

## Overview
SaladCat provides a convenient way to quickly scale hashcat deployments on Salad Cloud and Hashtopolis. Salad Cloud offers an affordable and efficient platform with access to a large pool of consumer-grade GPUs, making it ideal for this type of work.

## Features
- Quick deployment of hashcat on Salad Cloud
- Integration with Hashtopolis for distributed computing
- Automation scripts for easier management

## Getting Started

### Prerequisites
1. **Salad Cloud Account**
   - Requires an initial $50 deposit to get started.
2. **Hashtopolis Server**
   - A [Hashtopolis](https://github.com/hashtopolis/server) server running on any cloud service except Salad Cloud. 
   - For quick and easy deployment, refer to Nikita's [guide](https://nikita-guliaev.medium.com/clustering-hashcat-with-hashtopolis-for-distributed-cloud-computing-55f964a56804).

### Configuration
There are two essential environment variables that need to be configured on your Salad Container Group resource:

1. **API_SERVER_URL**
   - Format: `http://<hashtopolis_server_ip>:<port>/api/server.php`
2. **VOUCHER**
   - Value: Voucher code from your Hashtopolis server.

Ensure your Hashtopolis server is configured to allow a single voucher to be used multiple times. This can be set in `/config.php?view=5` under the "Vouchers can be used multiple times and will not be deleted automatically."

## Usage

### Automation Scripts
Two scripts are included to automate tasks:

1. **create_salad_hashcat.py**
   - Automates the creation of a new Salad Cloud container group.
   - Saves time by defining environment variables programmatically.

2. **update_agents.py**
   - Interacts with the Hashtopolis API to configure agents as trusted and to ignore errors.
   - Optionally assigns an agent to a specific task number.
   - Useful for managing multiple cracking nodes for a specific task.

## Contributions
Contributions to improve the project are welcome. If you find ways to optimize the Docker container or improve functionality, please feel free to submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any questions or support, please reach out via GitHub issues or contact the project maintainer at [your-email@example.com](mailto:your-email@example.com).
