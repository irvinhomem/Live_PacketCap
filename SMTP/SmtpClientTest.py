import smtplib
import logging
import csv
import os.path

from email.mime.text import MIMEText


class SmtpClientTest(object):

    def __init__(self):
        #Configure Logging
        logging.basicConfig(level=logging.INFO)
        # logging.basicConfig(level=logging.WARNING)
        self.logger = logging.getLogger(__name__)
        # self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.WARNING)

        #__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        #configs_file_name = "configs/smtp_configs.csv"
        #self.configs_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(configs_file_name)))
        self.configs_path ="./configs/smtp_configs.csv"
        self.configs_dict = {}
        self.creds_path = "../creds/smtp_creds.csv"
        self.creds_dict = {}

        self.smtp_serv_fqdn = ""
        self.smtp_serv_port = ""
        self.email_address_login = ""
        self.email_pass = ""

        self.msg = ""
        self.server = None

        return

    def read_configs(self):
        self.logger.info("Looking for config file ...")
        csv_filepath = self.configs_path
        # Make sure to strip the spaces from the credentials being added from the file into the configs object and obj parameters
        with open(csv_filepath, mode='r', newline='') as csvfile:
            domain_name_rdr = csv.reader(csvfile, delimiter=',')
            self.logger.info("Opened config file ...")
            for row in domain_name_rdr:
                if row[0] == 'fqdn':
                    self.configs_dict['server_fqdn'] = row[1].strip()
                    self.smtp_serv_fqdn = row[1].strip()
                elif row[0] == 'port':
                    self.configs_dict['server_port'] = row[1].strip()
                    self.smtp_serv_port = row[1].strip()
                # elif row[0] == 'user_email':
                #     self.configs_dict['user_email'] = row[1].strip()
                #     self.email_address_login = row[1].strip()
                # elif row[0] == 'pwd':
                #     self.configs_dict['pwd'] = row[1].strip()
                #     self.email_pass = row[1].strip()
                else:
                    self.logger.debug("Unknown config parameter found")

        self.logger.debug("Server FQDN: [%s]" % (self.configs_dict['server_fqdn']))
        self.logger.debug("Server Port: [%s]" % (self.configs_dict['server_port']))
        # self.logger.debug("User Email: [%s]" % (self.configs_dict['user_email']))
        # self.logger.debug("Pass: [%s]" % (self.configs_dict['pwd']))

    # NEEDS TO BE FIXED
    def get_emails_n_creds(self):
        self.logger.info("Looking for creds file ...")
        csv_filepath = self.creds_path
        # Make sure to strip the spaces from the credentials being added from the file into the configs object and obj parameters
        with open(csv_filepath, mode='r', newline='') as csvfile:
            domain_name_rdr = csv.reader(csvfile, delimiter=',')
            self.logger.info("Opened creds file ...")
            for row in domain_name_rdr:
                if row[0] == 'fqdn':
                    self.configs_dict['server_fqdn'] = row[1].strip()
                    self.smtp_serv_fqdn = row[1].strip()
                elif row[0] == 'port':
                    self.configs_dict['server_port'] = row[1].strip()
                    self.smtp_serv_port = row[1].strip()
                # elif row[0] == 'user_email':
                #     self.configs_dict['user_email'] = row[1].strip()
                #     self.email_address_login = row[1].strip()
                # elif row[0] == 'pwd':
                #     self.configs_dict['pwd'] = row[1].strip()
                #     self.email_pass = row[1].strip()
                else:
                    self.logger.debug("Unknown config parameter found")

        self.logger.debug("Server FQDN: [%s]" % (self.configs_dict['server_fqdn']))
        self.logger.debug("Server Port: [%s]" % (self.configs_dict['server_port']))
        # self.logger.debug("User Email: [%s]" % (self.configs_dict['user_email']))
        # self.logger.debug("Pass: [%s]" % (self.configs_dict['pwd']))

    def connect_to_SMTP_serv(self):
        self.server = smtplib.SMTP(self.smtp_serv_fqdn, self.smtp_serv_port)  # port 465 or 587
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(self.email_address_login, self.email_pass)

    def get_email_msg(self):
        self.msg = 'Hello world.'

    def send_single_email(self):
        self.email_FROM = self.user_actual_name+ "<"+ self.email_address_login + ">"
        self.email_TO = self.email_TO

        self.server.sendmail(self.email_FROM, self.email_TO, self.msg)
        self.server.close()


smtpClient = SmtpClientTest()
smtpClient.read_configs()

smtpClient.connect_to_SMTP_serv()
smtpClient.get_email_msg()
smtpClient.send_single_email()
