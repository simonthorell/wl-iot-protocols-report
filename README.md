# Wireless IoT Protocol Report

This repository is designed to facilitate collaborative work on a comprehensive report about Wireless IoT Protocols using markdown formatting. It leverages a Continuous Integration (CI) pipeline, which utilizes Python scripts to automatically merge markdown files into a single document and generate illustrative diagrams using matplotlib. Once a pull request is made to the main branch, the pipeline also compiles these materials into a PDF document.

## Usage Instructions

### Setting Up and Making Changes

1. **Clone the Repository:**
   Clone the repository to your local machine to start working on the report.
   ```
   git clone https://github.com/simonthorell/wl-iot-protocols-report.git
   cd wl-iot-protocols-report
   ```

2. **Create a New Branch:**
   Work on a new branch to encapsulate your changes.
   ```
   git checkout -b <YOUR-BRANCH-NAME>
   ```
   Replace `<YOUR-BRANCH-NAME>` with your desired branch name.

3. **Edit the Markdown Files:**
   Make your contributions by editing or adding markdown files within the `protocols` folder.

4. **Update Your Branch:**
   Before finalizing your changes, ensure your branch is updated with the latest main branch content.
   ```
   git pull origin main
   ```

5. **Commit Your Changes:**
   Add and commit the changes you've made to your branch.
   ```
   git add protocols/<YOUR-PROTOCOL>.md
   git commit -m "<YOUR-COMMIT-MESSAGE>"
   git push --set-upstream origin <YOUR-BRANCH-NAME>
   ```

### Creating and Merging Pull Requests

6. **Open a Pull Request on GitHub:**
   Navigate to the [repository on GitHub](https://github.com/simonthorell/wl-iot-protocols-report), switch to the `Pull requests` tab, and create a new pull request from your branch to the main branch.

7. **CI Pipeline Execution:**
   The CI pipeline will automatically execute Python scripts to merge all markdown files into a comprehensive `REPORT.md` and use another script to create necessary diagrams. Subsequently, it will compile these into a `REPORT.pdf` in the `pdfs` folder.

### Important Note for Merging

- **Review Requirement:**
  Your pull request may require review. Ensure that it is reviewed by a team member or a repository administrator before proceeding. You can request a review through the GitHub interface.

- **CI Completion:**
  Due to a GitHub Actions/Workflows limitation, wait for all CI pipeline jobs to complete successfully before merging your pull request into the main branch. Merging prematurely might result in your changes not being correctly reflected in the master files.