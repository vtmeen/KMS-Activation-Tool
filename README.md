<p align="center"><img src="https://i.ibb.co/Qdhc8hC/KMS-Activation-Tool-Logo.png" alt="KMS-Activation-Tool"></p>

<p align="center">
  <img src="https://img.shields.io/badge/windows%20cmd-4D4D4D?style=for-the-badge&logo=windows%20cmd&logoColor=white" 
</p>

<h1 align="center">Key Management Service - Activation-Tool</h1>



### 🗒️About
This is a straightforward tool for handling Windows activation through KMS (`Key Management Service`) servers. It’s designed to connect your system to a trusted KMS server and execute key activation commands seamlessly.

<hr>
</hr>

### ⚙️What It Does:
* **Connects to a KMS server (`default: kms.digiboy.ir`) to manage activation.**
* **Allows you to activate Windows using pre-configured KMS client keys for various editions like Pro, LTSC, and more.**
* **Offers commands to deactivate Windows, check activation status, or complete the activation process.**
* **Supports both English and Russian for easy navigation.**
* **~~Logs every action in a detailed file for transparency and troubleshooting.~~**

<hr>
</hr>

### 🔧How It Works:
<details>

<summary>Troubleshooting & Help</summary>

**If you experience any issues with the activation process, here are some troubleshooting tips:**
   - Ensure your internet connection is stable. The tool requires an active connection to the KMS server.
   - Run the tool with <ins>Administrator rights</ins> to avoid permission issues.
   - For more information on KMS client activation keys and troubleshooting steps, please refer to [KMS documentation](https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys?tabs=server2025%2Cwindows1110ltsc%2Cversion1803%2Cwindows81).


</details>

<details>

<summary> See It in Action </summary>

![kms](https://github.com/user-attachments/assets/a5833e6a-2032-4a26-b697-e51668f6c718)

</details>

1. The tool connects to one of the supported KMS servers.
2. The server responds with the activation status or any relevant messages.
3. It sends commands like:

<hr>
</hr>

- ✉️`slmgr /skms [server_address]` — Configures the KMS server.
   >![wscript_TOg7yzubqW](https://github.com/vtmeen/KMS-Activation-Tool/blob/main/pic/401530279-f45a0981-adec-4e6b-a52c-c384e6cdbd23.png)

- 🔑`slmgr /ipk [product_key]` — Installs the KMS client key for the selected Windows edition.
   > ![wscript_4CNWMlPWgI](https://github.com/vtmeen/KMS-Activation-Tool/blob/main/pic/401533422-472e58d1-4668-40e3-842a-1d4e1043b044.png) 
   
- ✅`slmgr /ato` — Activates the installed key.
   > ![wscript_LRsIye3Jwn](https://github.com/vtmeen/KMS-Activation-Tool/blob/main/pic/401533550-68015edd-d9f3-4dc4-a903-0546dc7b0768.png)

<p align="center"> PROFIT! Windows is activated and updates are working

<hr>
</hr>

> [!NOTE]
> - Completely Free & Open Source: Modify and adapt it as you see fit.
> - Lightweight and Straightforward: Focused solely on Windows activation without any extra bloat.
> - Always Up-to-Date: Maintained for compatibility with the latest Windows editions.

```
First Release date - Jan-10-2025
Latest Version 1.0
```

<hr>
</hr>

<p align="center"> Activate with ease. Built for everyone🫂
