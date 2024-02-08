# Wireless IoT Protocol Report

This repo is a setup to enable collaboration work in the same report using markdown formatting.  
The CI pipeline is setup to automatically merge the markdown-files and generate a PDF once making a pull request to the main branch.

## Usage
1) Clone this repo:
```bash
git clone https://github.com/simonthorell/wl-iot-protocols-report.git
git init
git remote add origin https://github.com/simonthorell/wl-iot-protocols-report.git
```
2) Create a new branch from main:
```bash
git checkout -b <YOUR-BRANCH-NAME>
```
3) Edit the markdown file for the protocol in the `protocols` folder.
4) Ensure your branch are up to date with main before commiting:
```bash
git pull origin main
```
5) Add and commit your changes:
```bash
git add protocols/<YOUR-PROTOCOL>.md
git commit -m "<YOUR-COMMIT-MESSAGE"
git push
```
6) Open Github [repo](https://github.com/simonthorell/wl-iot-protocols-report) and make a new Pull Request from your branch to main under the tab `Pull requestes`.
7) The first stage of the CI will automatically merge all the markdown-files into a `REPORT.md`, and the second stage will automatically generate the file `REPORT.pdf` in the pdfs-folder.
  

## IMPORTANT NOTE !
Due to a bug in GitHub Actions/Workflows, you will need to wait until all jobs have finished before you merge your `Pull Request` to main.
If you merge before completion your changes will not be written into the master-files in main. Please make sure all actions completed before you merge!