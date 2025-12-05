# Secure Cloud File Sharing using Blockchain and CP-ABE

A secure, decentralized file sharing application that combines **Django**, **Ethereum Blockchain**, and **Google Drive** storage. This project ensures data privacy through **AES encryption** and manages access control via a **Smart Contract** on the Ethereum network.

## 🚀 Features

* **Dual Role System:** Separate workflows for **Data Owners** and **Data Users**.
* **Secure Storage:** Files are encrypted using **AES-256** before being uploaded to **Google Drive**.
* **Blockchain Access Control:** File metadata, access policies, and permission grants are stored immutably on the **Ethereum Sepolia Testnet**.
* **Decentralized Key Management:** Uses polynomial interpolation (Secret Sharing) concepts for managing encryption keys on-chain.
* **Access Request Mechanism:** Users can request file access, which Owners can approve or reject via the blockchain.
* **Automated Auditing:** All uploads, requests, and grants are recorded as transactions on the blockchain.

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Blockchain:** Solidity (Smart Contracts), Web3.py
* **Storage:** Google Drive API v3
* **Cryptography:** PyCryptodome (AES, SHA256)
* **Frontend:** HTML, CSS, JavaScript

## 📂 Project Structure

The project directory should be organized as follows:

```text
miniproject_latest/
├── db.sqlite3                  # Django Database
├── manage.py                   # Django CLI
├── credentials.json            # Google API Credentials (You must provide this)
├── miniproject/                # Project Configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── mp/                         # Main Application 
    ├── admin.py
    ├── apps.py
    ├── models.py               # Database Models (RegUser, File, Subscription)
    ├── new1.py                 # Blockchain & Crypto Logic
    ├── newsol1.sol             # Solidity Smart Contract
    ├── newabi.json             # Contract ABI
    ├── templates/              # HTML Files
    └── views.py                # View Logic****
```
## ⚙️ Prerequisites
Python 3.10+ installed.

MetaMask wallet with Sepolia Testnet ETH.

Infura API Key (for connecting to Sepolia).

Google Cloud Console project with Drive API enabled.

## 📦 Installation & Setup
1. Clone and Prepare Directories
Extract the project. Important: Ensure the inner folder named "Secure Cloud File Sharing Project" is renamed to mp to match the Django app configuration.

2. Create Virtual Environment

```bash

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```
3. Install Dependencies
Run the following command to install the required libraries:


```bash

pip install django web3 google-auth google-auth-oauthlib google-api-python-client pycryptodome requests
```
### 4. Configure Google Drive API

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the **Google Drive API**.
3. Create OAuth 2.0 Credentials and download the JSON file.
4. Rename it to `credentials.json` and place it in the root directory (next to `manage.py`).

### 5. Configure Blockchain

1. **Deploy Smart Contract:**
   - Copy the code from `mp/newsol1.sol` to [Remix IDE](https://remix.ethereum.org/).
   - Compile and Deploy it to the **Sepolia Testnet**.
   - Copy the **Contract Address**.

2. **Update `mp/new1.py`:**
   - Update `CONTRACT_ADDRESS` with your deployed contract address.
   - Update `BLOCKCHAIN_URL` with your Infura/Alchemy endpoint if needed.

3. Ensure `mp/newabi.json` contains the ABI array from Remix.

Here is the text formatted exactly like your examples:

### 6. Setup Configuration File (credentials.py)

1. **Create a new file named credentials.py inside your main application folder (e.g., mp/credentials.py).**

1. **Paste the following code structure and replace the placeholder values with your actual data:**

```Python

# mp/credentials.py

# --------------------------
# BLOCKCHAIN CONFIGURATION
# --------------------------
# The Contract Address obtained after deploying to Sepolia
CONTRACT_ADDRESS = "0xYourDeployedContractAddressHere"

# The RPC Endpoint (Infura, Alchemy, or Localhost)
BLOCKCHAIN_URL = "https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID"

# --------------------------
# GOOGLE DRIVE CONFIGURATION
# --------------------------
# Path to the Google Credentials JSON file
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"

# --------------------------
# APP SETTINGS
# --------------------------
ENCRYPTION_ALGO = "AES"
```

### 7. Database Setup
```bash

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser # Optional, for admin access
```

### 8. Run the Application
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser.

## 📖 How to Use
### 1. Registration & Login
   - Register a new account. Crucial: You must provide a valid Ethereum Private Key during registration to sign blockchain transactions.

   - Login with your credentials.

### 2. Data Owner Workflow
   - Select "Data Owner" on the dashboard.

   - Upload File: Choose a file, specify a department/policy. The file is encrypted, uploaded to Drive, and metadata is sent to the blockchain.
   - <img width="1482" height="341" alt="image" src="https://github.com/user-attachments/assets/20d5aa56-b8ee-412d-9dcd-a5eab8693534" />


   - Grant Access: View pending requests from users and approve them. This sends the decryption key (encrypted) to the blockchain.

   - Revoke Access: Remove a user's ability to decrypt a specific file.

### 3. Data User Workflow
   - Select "User" on the dashboard.

   - Request Access: Enter the filename you wish to access. A request transaction is sent to the blockchain.

   - Download: Once approved, enter the filename. The system fetches the encrypted file from Drive, retrieves the key from the blockchain, decrypts it locally, and downloads it to your machine.
<img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/253be7b3-fd24-4915-86a5-6c1ccbbd90d5" />
<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/37f631c0-2932-4b56-8bf5-ad78e3f24a59" />
<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/f3efe6ef-816b-4ad4-aca7-ba0021f14937" />
<img width="1920" height="1080" alt="4" src="https://github.com/user-attachments/assets/e8c4614a-3340-416b-938a-10f11e05ce77" />
<img width="1920" height="1080" alt="5" src="https://github.com/user-attachments/assets/daac32fa-a19a-4e27-b9d3-960c6d15b7e7" />
<img width="1920" height="1080" alt="6" src="https://github.com/user-attachments/assets/c9240ce9-dfae-45d7-a83a-108f023bafee" />
<img width="1920" height="1080" alt="7" src="https://github.com/user-attachments/assets/4a6e4f07-de9e-4339-995f-79363ca05ab2" />
<img width="1920" height="1080" alt="8" src="https://github.com/user-attachments/assets/bba1e948-097d-4150-8882-7a88de27392e" />
<img width="1920" height="1080" alt="9" src="https://github.com/user-attachments/assets/aaf8ed58-86c7-4c8a-8296-ba67de5ccb4c" />
<img width="1920" height="1080" alt="10" src="https://github.com/user-attachments/assets/8e68aa69-ccb4-42d6-b365-36d2e90aa77e" />
<img width="1920" height="1080" alt="11" src="https://github.com/user-attachments/assets/3785c7f0-f5a3-4c6f-aae6-ee5720c70f28" />
<img width="1920" height="1080" alt="12" src="https://github.com/user-attachments/assets/b31abebc-9b0c-43c2-ba02-37c642d88c21" />
<img width="1920" height="1080" alt="13" src="https://github.com/user-attachments/assets/0f4c261c-d916-468f-9c26-1522a6fbfd81" />
<img width="1920" height="1080" alt="14" src="https://github.com/user-attachments/assets/42275993-a616-4a45-9372-660864b59d46" />
<img width="1920" height="1080" alt="15" src="https://github.com/user-attachments/assets/f4eef98a-6c28-4cf3-a52c-3b7a2aca2fe2" />
<img width="1920" height="1080" alt="16" src="https://github.com/user-attachments/assets/2808d767-c998-4c1b-a0dd-2cdb5914c6c4" />
<img width="1920" height="1080" alt="17" src="https://github.com/user-attachments/assets/22ce23ff-5f3f-4aa7-abe4-57c5ab56ed9d" />
<img width="1920" height="1080" alt="18" src="https://github.com/user-attachments/assets/29d7c9d0-4b3b-4a26-9d77-af421a0c75d3" />


## ⚠️ Important Notes
Security: Never share your credentials.json or your Ethereum Private Key.

Google Token: On the first run, a browser window will open to authenticate with Google. This creates a token.json file automatically.

Nonce Errors: The system handles transaction nonces manually to allow batch processing. If you see "nonce too low" errors, restart the server or check pending transactions in MetaMask.

## 📄 License
This project is for educational purposes.
