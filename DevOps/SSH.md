## SSH - Server Basics:

### **1. What is a server?**
A server is a computer or software program that provides functionality or services to other devices, known as clients, within a network. Servers are designed to handle requests from clients, such as serving web pages, processing database queries, or delivering files.

### **2. Where servers usually live?**
Servers typically reside in centralized locations optimized for connectivity, security, and infrastructure resources. Common locations include:

- **Data Centers:** Specialized facilities equipped with power, cooling, and networking infrastructure to host servers. Data centers offer physical security and redundancy to ensure high availability.

- **Cloud Environments:** Virtualized infrastructure provided by cloud service providers like AWS, Google Cloud, or Azure. Servers in the cloud are accessed and managed remotely, offering scalability and flexibility.

Understanding server basics is essential for deploying and managing software applications and services in real-world projects.

## SSH - SSH and Bash Scripting:

### **1. What is SSH?**
SSH (Secure Shell) is a cryptographic network protocol used for secure remote communication between two computers. It provides encrypted communication sessions over unsecured networks, such as the internet, ensuring confidentiality and integrity of data transmission. SSH is commonly used for remote login, command execution, file transfer, and tunneling.

### **2. How to create an SSH RSA key pair?**
To create an SSH RSA key pair, follow these steps:

1. Open a terminal or command prompt.
2. Use the `ssh-keygen` command to generate the key pair.
   ```bash
   ssh-keygen -t rsa
   ```
3. Follow the prompts to specify the file path and passphrase for the key pair.
4. The public key (`id_rsa.pub`) and private key (`id_rsa`) will be generated in the specified directory.

### **3. How to connect to a remote host using an SSH RSA key pair?**
To connect to a remote host using an SSH RSA key pair, follow these steps:

1. Copy the public key (`id_rsa.pub`) to the remote host's `~/.ssh/authorized_keys` file.
   ```bash
   ssh-copy-id user@remote_host
   ```
2. Ensure proper permissions are set on the `~/.ssh` directory and the `authorized_keys` file.
   ```bash
   chmod 700 ~/.ssh
   chmod 600 ~/.ssh/authorized_keys
   ```
3. Use the `ssh` command to connect to the remote host.
   ```bash
   ssh user@remote_host
   ```

### **4. The advantage of using #!/usr/bin/env bash instead of /bin/bash?**
Using `#!/usr/bin/env bash` in shebang line allows for better portability and environment handling compared to `#!/bin/bash`. It ensures that the correct bash interpreter is located regardless of its location in the filesystem. This is particularly useful when scripts need to run on different systems where bash may be installed in different locations.

## SSH - Writing a Bash Script to Connect Using a Private Key

To fulfill the requirements of connecting to a server using SSH with a private key and the user `ubuntu`, we will create a Bash script named `0-use_a_private_key`. Below is the script with single-character flags for SSH:

```bash
#!/bin/bash

ssh -i ~/.ssh/school ubuntu@server01
```

Explanation of the script:

- `#!/bin/bash`: Specifies the Bash interpreter.
- `ssh`: Initiates an SSH connection.
- `-i ~/.ssh/school`: Specifies the private key file to use for authentication.
- `ubuntu@server01`: Specifies the user (`ubuntu`) and the server (`server01`) to connect to.

After creating the script, make it executable using `chmod +x 0-use_a_private_key`. Then, run the script using `./0-use_a_private_key` to connect to the server using SSH with the specified private key and user.

Upon successful execution, the output should display the SSH connection to the server, and upon exiting, the connection to the server will be closed.

Example usage:

```bash
sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
sylvain@ubuntu$
```

In this example, the script successfully connects to the server `server01` using the private key `~/.ssh/school` and the user `ubuntu`.

## SSH - Creating an SSH Key Pair

To fulfill the requirements of creating an RSA key pair with a passphrase, we will write a Bash script named `1-create_ssh_key_pair`. Below is the script to generate the key pair:

```bash
#!/bin/bash

# Set the file path for the private key
private_key="school"

# Generate the RSA key pair with 4096 bits and protect it with the passphrase "betty"
ssh-keygen -t rsa -b 4096 -C "ALX SSH Key" -f "$private_key" -q -N "betty"
```

Explanation of the script:

- `#!/bin/bash`: Specifies the Bash interpreter.
- `private_key="school"`: Defines the file name for the private key.
- `ssh-keygen`: Command to generate SSH keys.
  - `-t rsa`: Specifies the type of key to create (RSA).
  - `-b 4096`: Specifies the number of bits in the key (4096).
  - `-C "ALX SSH Key"`: Adds a comment to the key (optional).
  - `-f "$private_key"`: Specifies the file name of the private key.
  - `-q`: Suppresses unnecessary output.
  - `-N "betty"`: Specifies the passphrase for the key.

After creating the script, make it executable using `chmod +x 1-create_ssh_key_pair`. Then, run the script using `./1-create_ssh_key_pair` to generate the SSH key pair.

Upon successful execution, the script will generate the RSA key pair with the specified file name (`school`) and passphrase (`betty`). The private key (`school`) and public key (`school.pub`) will be created in the current directory.

Example usage:

```bash
sylvain@ubuntu$ ls
1-create_ssh_key_pair
sylvain@ubuntu$ ./1-create_ssh_key_pair
sylvain@ubuntu$ ls
1-create_ssh_key_pair  school  school.pub
sylvain@ubuntu$
```

In this example, the script successfully generates an RSA key pair with the private key named `school` and the passphrase `betty`.

## SSH - Client Configuration File

To configure the SSH client to use the private key `~/.ssh/school` and refuse password authentication, you need to modify the SSH client configuration file. Below is an example of how to configure the SSH client to meet these requirements:

```bash
# SSH Client Configuration File

# Use the private key ~/.ssh/school for authentication
IdentityFile ~/.ssh/school

# Disable password authentication
PasswordAuthentication no
```

Explanation of the configuration:

- `IdentityFile ~/.ssh/school`: Specifies the path to the private key to use for authentication. Here, it is set to `~/.ssh/school`.
  
- `PasswordAuthentication no`: Disables password authentication, ensuring that only public key authentication is attempted.

After adding these configurations to your SSH client configuration file, you will be able to connect to servers without typing a password, provided that the corresponding public key is added to the server's `authorized_keys` file.

Example usage:

```bash
sylvain@ubuntu$ ssh -v ubuntu@98.98.98.98
```

In this example, the SSH client attempts to authenticate using the private key `~/.ssh/school` and does not attempt to authenticate using a password. Replace `98.98.98.98` with the IP address of your server for testing purposes.

## SSH - Let me in!

To allow you access to the server, you need to add your SSH public key to the server's `authorized_keys` file. Below is the SSH public key that you can add to the server for the `ubuntu` user:

```plaintext
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
```

To add the key to the server, follow these steps:

1. Log in to your server using SSH.
2. Open the `authorized_keys` file for the `ubuntu` user:
   ```bash
   nano ~/.ssh/authorized_keys
   ```
3. Paste the SSH public key into the file.
4. Save and close the file.

After adding the public key to the `authorized_keys` file, you will be able to connect to the server using the private key corresponding to this public key.

This process allows secure access to the server without the need for a password.

## SSH - Client Configuration File (w/ Puppet)

In this task, we will use Puppet to configure the SSH client configuration file (`~/.ssh/config`) to enable passwordless authentication using a private key.

### Requirements:

1. **SSH Client Configuration:**
   - Configure the SSH client to use the private key `~/.ssh/school`.
   - Configure the SSH client to refuse authentication using a password.

### Puppet Manifest Example:

```puppet
# File: 100-puppet_ssh_config.pp

file { '/home/ubuntu/.ssh/config':
  ensure  => present,
  mode    => '0644',
  content => "
    Host *
        PasswordAuthentication no
        IdentityFile ~/.ssh/school
  ",
}
```

### Explanation:

- The Puppet manifest creates or updates the SSH client configuration file (`~/.ssh/config`) for the `ubuntu` user.
- It ensures that password authentication is disabled (`PasswordAuthentication no`) and specifies the private key (`IdentityFile ~/.ssh/school`) to be used for authentication.

### Applying the Puppet Manifest:

```bash
$ sudo puppet apply 100-puppet_ssh_config.pp
```

Upon execution, Puppet will apply the specified configuration changes to the SSH client configuration file.

### Real-World Application:

In real-world projects, Puppet is commonly used for configuration management to automate the setup and maintenance of servers and applications. By defining infrastructure as code, Puppet ensures consistency, reliability, and security across server environments. This SSH client configuration example demonstrates how Puppet can be leveraged to enforce secure authentication practices across multiple servers, enhancing overall system security.

© [2024] [Paschal Ugwu]
