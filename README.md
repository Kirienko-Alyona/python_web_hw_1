This bot supports the following commands:

| Example command                                     | Command description
|-----------------------------------------------------|------------------------------------------------------------------
| add Natally                                         | I will save the friend's name
| edit contact Natally                                | I will correct the name of an existing contact
| show all                                            | I will show the entire list of contacts / all contacts
| del contact Natally                                 | I will delete the contact
| add phone Natally 096-45-34-876                     | I will add a number to your contact
| change phone Natally 0995456743 0986754325          | I will change your friend's phone number
| phone Natally                                       | I will show your friend's phone, just enter the name
| del phone Natally 096-45-34-876                     | I will delete your contact's phone number
| add mail Vasya vasiliy007@gmail.com                 | I will add email to your contact
| change mail Vasya new_mail_vasya@gmail.com          | I will change email of your contact
| del mail Vasya                                      | I will delete email of your contact
| add birth Natally 1999.12.23                        | I will add the birthday of your friend
| change birth Natally 1999.12.23                     | I will change your friend's date of birth
| all births 50                                       | I will show the birthdays of all your friends in the next 50 days
| days to birth Leo                                   | I will tell you the number of days until my friend's birthday
| del birth Natally                                   | I will delete your contacts's birthday
| add note Natally str. Peremogy, house 76.           | I will add notes to the contact
| change note Natally str. Gagarina, h.126.           | I will change the contact notes
| del note Natally                                    | I will delete contact notes
| add tag Natally #address #favorite                  | I will add tags
| find tag #favorite                                  | I will show notes with such tags
| del tags Natally                                    | I will delete a note's tags
| help                                                | I will tell you about my possibilities
| sort                                                | I will sort all the files in the folder you choose
| find mi                                             | I will find all record, which contains 'mi'
| ('good bye', 'exit', 'close', 'quit', 'bye', 'q')   | Enter one of these word and I will finish my work
|__________________________________________________________________________________________________________________________

In order to install this application in the folder with the file setup.py in the command line enter:

pip install .