# Wireless IoT Protocol Report

This repo is a setup to enable collaboration work in the same report using markdown formatting.  
The CI pipeline is setup to automatically merge the markdown-files and generate a PDF once making a pull request to the main branch.

## Usage
1) Create a new branch from main:
```bash
git checkout -b <YOUR-BRANCH-NAME>
```
2) Edit the markdown file for the protocol in the `protocols` folder.
3) Add and commit your changes:
```bash
git add protocols/<YOUR-PROTOCOL>.md
git commit -m "<YOUR-COMMIT-MESSAGE"
git push
```
4) Before creating a Pull Request, make sure your branch is up to date with main:
```bash
git merge main
```
5) If updates where pulled, please redo step 3 to push latest changes. 
6) Open Github [repo](https://github.com/simonthorell/wl-iot-protocols-report) and make a new Pull Request from your branch to main under the tab `Pull requestes`. 
7) The first stage of the CI will automatically merge the markdown-files into a `REPORT.md`, and the second stage will automatically generate the file `REPORT.pdf` in the pdfs-folder.