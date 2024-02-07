from pathlib import Path

def load_protocol_content(protocol_name, protocols_path='protocols'):
    """
    Load the content of a markdown file based on the protocol name.
    """
    file_path = Path(protocols_path) / f"{protocol_name}.md"
    try:
        return file_path.read_text()
    except FileNotFoundError:
        return f"Content for {protocol_name} not found."

def main():
    stub_path = Path('docs/REPORT.stub')
    report_path = Path('docs/REPORT.md')
    protocols_path = 'protocols'
    
    # Read the stub content
    report_content = stub_path.read_text()
    
    first_replacement = True
    # List of protocol names to replace in the stub
    protocols = ['WIFI', 'BLUETOOTH', 'BLUETOOTH_LE', 'ZIGBEE', 'ZWAVE', 'NFC']
    
    # Replace each placeholder with the corresponding markdown content
    for protocol in protocols:
        content = load_protocol_content(protocol, protocols_path=protocols_path)
        # Add a new line between each markdown file content
        if first_replacement:
            # For the first replacement, remove the leading newline to avoid an extra line at the beginning
            content = content.lstrip("\n<br/>\n")
            first_replacement = False
        report_content = report_content.replace(f'{{{protocol}}}', content)
    
    # Save the updated content to REPORT.md
    report_path.write_text(report_content)

if __name__ == "__main__":
    main()