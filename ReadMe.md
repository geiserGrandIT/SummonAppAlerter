# Summon Alerter
## What is it?
Summon Alerter is a program that detects whether a customer has requested a vehicle and plays a professional sound that alerts 
The Valet at a Computer terminal. For some reason App developers think that people don't want or need to use computers and 
everyone has a smartphone, which is not the case.
This is designed to work EXCLUSIVELY with Summon Operator at https://Summon.tech

## How does it work?
It works by detecting changes in HTML then running logic based on those changes. It does this inside of a selenium ran Chrome 
Browser. 

## TroubleShooting
### Summon isn't logging into the website
Restart/Reinstall the App on the Tablet and re-sign in. Yes that is right, you have to be signed in on the app in order to use
the computer, what a world.

### Summon won't stop saying 'a guest has requested a vehicle'
This program will need tweaking on occasion as Summon Operator changes their HTML on their app.
If Summon Alerter is constantly alerting that a customer has requested a vehicle, and there is no vehicle, check
either the logs or the terminal running with the program. If there is a line about not being able to find path or
Xpath this is how you can solve the issue.

Open the Summon alerter app, Right click on the Request hand icon. select Inspect. Then right click the Request 
hand again and select request a second time. This will take you to the location of the hand image itself. Then 
move up the HTML tree until you find the following element:

<ion-tab-button _ngcontent-ng-c546626328="" class="md tab-has-label tab-has-icon tab-layout-icon-top ion-activatable ion-selectable ion-focusable hydrated"><ion-icon _ngcontent-ng-c546626328="" name="hand-left" role="img" class="md hydrated"></ion-icon><ion-label _ngcontent-ng-c546626328="" class="ion-text-uppercase sc-ion-label-md-h sc-ion-label-md-s md hydrated"><b _ngcontent-ng-c546626328="">Request</b></ion-label><!----></ion-tab-button>

right click on the element in the elements view and go to copy, then find copy full XPath. Click that. 

Open Xpaths.cfg in NotePad and replace the line request=/some/sort/of/XPath with request=/Pasted/Content
it will look like something like request=/html/body/app-root/ion-app/ion-router-outlet/app-location/ion-footer/ion-tab-bar/ion-tab-button[3]

ion-tab-button[3] should be the last thing mentioned on the request line. 

Save the document and close it.
restart Summon Alerter.