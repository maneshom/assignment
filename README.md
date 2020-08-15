=========
Assignment
==========

Assignment is a Django project enable email marketing.User can save/edit/delete email addresses of subscriber and customer. User can send email(including subject and body) to them. And user can save email content as draft.User can use that draft content as new email.An option for select multiple or all email is added in email compose page.List option added in all pages(contact, draft, email sent). So user can search particular item, filter specific items and sort items using list table.

Here Email configured for local development purpose only.

Quick start
-----------
1. Create a virtual environment(example:assignment_env) with python 3.8(tested only in this version)
2. Activate environment and install packages listed in reqirements.txt
3. Run dumb SMTP server inside a new terminal window using ,

  python -m smtpd -n -c DebuggingServer localhost:1025
  
  This server prints to standard output all email headers and the email body.User can verify the content. 
4. Start the development server and visit http://127.0.0.1:8000/marketing/
5. Login using username: test_user, and password: @password
6. Select each menu items based on requirement

  
