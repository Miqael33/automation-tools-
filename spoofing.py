import imaplib  # Importing the IMAP library to connect to an email server
import email  # Importing the email library to parse email messages
from termcolor import cprint  # Importing cprint function from termcolor library for colored printing

def emailSpoofDetection(header, emailDomain):
    # Checking for keywords in the email header
    if 'Dear Customer' in header:
        return False  # If "Dear Customer" is found, consider the email as spoofed

    # Checking the email content for a link to a non-authentic site
    if 'Click here to update your password' in header or 'Click the link below' in header:
        return False  # If the email contains a suspicious link, consider it as spoofed

    # Add other checking scenarios here if needed
    if 'Barev' in header:  # Checking for a specific keyword in the header
        return False

    # If none of the above conditions are met, consider the email as genuine
    return True

def connect_to_mailbox(username, password):
    # Connecting to the mailbox server
    mail = imaplib.IMAP4_SSL('imap.gmail.com')  # Connecting to the Gmail IMAP server over SSL
    mail.login(username, password)  # Logging into the mailbox with the provided credentials
    return mail  # Returning the mailbox connection object

def analyze_emails(mail, emailDomain):
    mail.select('inbox')  # Selecting the inbox folder for analysis

    # Fetching all emails in the inbox folder
    result, data = mail.search(None, 'ALL')

    if result == 'OK':
        email_ids = data[0].split()  # Splitting the email IDs obtained from the search result
        for email_id in email_ids:
            result, data = mail.fetch(email_id, '(RFC822)')  # Fetching the email message

            if result == 'OK':
                raw_email = data[0][1]  # Extracting the raw email message
                msg = email.message_from_bytes(raw_email)  # Parsing the email message
                header = msg.as_string()  # Converting the email headers to a string

                analysis = emailSpoofDetection(header, emailDomain)  # Performing spoof detection

                # Printing the analysis result with colored output
                if analysis:
                    cprint(f'Email {email_id.decode()} is fine!', 'yellow')  # If the email is genuine
                else:
                    cprint(f'Email {email_id.decode()} is a spoofing attempt!', 'red')  # If the email is spoofed

def main():
    username = input('Enter your email username: ')  # Asking for the email username
    password = input('Enter your email password: ')  # Asking for the email password
    emailDomain = input('Enter your email domain: ')  # Asking for the email domain

    mail = connect_to_mailbox(username, password)  # Connecting to the email mailbox
    analyze_emails(mail, emailDomain)  # Analyzing emails in the mailbox
    mail.logout()  # Logging out from the email server

if __name__ == "__main__":
    main()  # Running the main function when the script is executed
