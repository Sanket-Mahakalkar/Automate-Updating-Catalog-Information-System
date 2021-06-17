
#!/usr/bin/env python3
import os
from datetime import date
import pdf_reports
import emails
import Description_file

keys=['name', 'weight']
user=os.getenv('USER')
name_dict=[]
summary=''
weight_dict=[]
feedback_dict=[]
path='/home/{}/supplier-data/descriptions/'.format(user)
for file in os.listdir(path):
  feedback_dict.append(Description_file.file_system(path+file, ''))

for dict in feedback_dict:
   name_dict.append('name: '+dict['name'])
   weight_dict.append('weight: '+str(dict['weight']) + ' lbs')
for i in range(len(name_dict)):
  summary += name_dict[i] + '<br />' + weight_dict[i] + '<br />' + '<br />'

if __name__ == "__main__":
    filename='/tmp/processed.pdf'
    date=date.today().strftime('%B %d, %Y')
    title='Processed Update on ' + date
    pdf_reports.generate_report(filename, title, summary)
    sender='automation@example.com'
    recipient='student-02-01fa5d13df68@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    message=emails.generate_email(sender, recipient, subject, body, filename)
    emails.send_email(message)
