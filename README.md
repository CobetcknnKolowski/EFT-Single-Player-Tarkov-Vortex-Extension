# EFT-Single-Player-Tarkov-Vortex-Extension
This is an Extension for the Vortex Modding platform Created by Nexus Mods that allows you to use Vortex to manage your Single Player Tarkov mods.

Please Pardon the mess, This is all new to me from the Developer side. <br/>
Also, this page assumes you know how to use Vortex Mod Manager, If there's enough demand, I will attach a guide to using it. <br/>
---
<details open>
<summary>Installing/Updating the extension </summary>
  <div align="left">
    Go to the "Extensions" List in the Vortex app <br/>   
    <img width="238" height="410" alt="image" src="https://github.com/user-attachments/assets/1415c11c-7e1a-411f-a295-4d017e8e7b37" /> <br/> <br/>
    Click on the button in the bottom right and select the zip file you downloaded, "Vortex Extension Update - Escape From Tarkov - Single Player Tarkov Mod Vortex Extension Vx.x.x". <br/> 
    <img width="1297" height="155" alt="image" src="https://github.com/user-attachments/assets/f973fea5-ee8e-45d0-a0e7-357024a621ae" /> <br/> <br/>  
    Restart Vortex, and Search the "Extensions" List, if you see it, it successfuly installed, If not, Repeat install and restart. (I do not know why Multiple install attempts is needed sometimes) <br/> 
    <img width="612" height="187" alt="image" src="https://github.com/user-attachments/assets/193c7021-bb59-4ee2-8862-dfe9097e0e09" /> <br/> <br/>
    Go to the "Games" tab <br/> 
    <img width="259" height="544" alt="image" src="https://github.com/user-attachments/assets/f871b75a-c84b-4b9c-9788-c9c68a31dc0b" /> <br/> <br/>
    Search for "Tarkov" <br/>
    <img width="330" height="195" alt="image" src="https://github.com/user-attachments/assets/51401b8b-102c-43c7-889b-ea5a358feaba" /> <br/> <br/>
    Click on it to Activate and it should ask you where you have SPT installed, (Where are SPT.Server.exe and SPT.Launcher located). <br/> <br/>
    Congrats! Vortex can now handle your mod installs as well as activating or deactivating mods. <br/> <br/>
    To see where Vortex is downloading and staging your mods, go to the "Settings" List and check the "Mods" and "Download" Tabs, you can also change the paths for both if you have somewhere else you'd rather mods be stored. <br/> 
    <img width="1027" height="587" alt="image" src="https://github.com/user-attachments/assets/01885f83-763a-4b93-ac4f-8cd88f4e87b6" /> <br/>
  </div>
</details>

---
 
<details open>
<summary>Supported Tools</summary>
  <div align="left">
    Vortex allows you to create shortcuts to tools that can easily be accessed from your Vortex dashboard <br/>
    <img width="1924" height="357" alt="image" src="https://github.com/user-attachments/assets/40fa8a1a-53cb-4951-ad9a-dea6848558bf" /> <br/>  <br/>
    Included in the extension is the "SPT Server" and "SPT Launcher" exe's as well as the foundation for other popular Mod tools. <br/> 
    1. Server Value Manager, https://hub.sp-tarkov.com/files/file/379-server-value-modifier-svm/ <br/> 
    2. Load Order Editor Drag'n'Drop, https://hub.sp-tarkov.com/files/file/1923-load-order-editor-drag-drop/ <br/> 
    3. LOE - Load Order Editor, https://hub.sp-tarkov.com/files/file/1082-loe-load-order-editor/ <br/> 
    4. Acid's Bot Placement System, https://hub.sp-tarkov.com/files/file/2782-abps-acid-s-bot-placement-system/ <br/> <br/>
    
   **You will still need to download and install any of the above mods you wish to use into their expected (default) locations, I merely laid the basic file structure and pointers so that Vortex will instantly recognize and populate the shortcuts. Yes having Vortex handle the install is fine, in fact you should let Vortex handle as many of the installations as possible.**

  Note: If there is a tool you wish to see added to the list, Let me know and I will add it.
  </div>
</details>

---

<details>
<summary>Installing Mods</summary>
    <div align="left">
Unfortunately, It is not completely hands off endeavour if you want to take advantage of all the features of Vortex: Proper Deployment, Dependencies and the Variants systems. <br/> <br/>

First, We will need to make sure that the mod is packaged as Vortex expects. Let's use [Server Value Modifier](https://hub.sp-tarkov.com/files/file/379-server-value-modifier-svm/) as an example that requires manual intervention, Apologies for putting you on blast GhostFenixx xP.
<img width="769" height="55" alt="image" src="https://github.com/user-attachments/assets/0b448fd4-9ba4-4be6-b4da-7fc6624c25ac" /> <br/>

Next, We need to remove the extra periods in the filename, To make version reading easier, I use dashes.
<img width="758" height="43" alt="image" src="https://github.com/user-attachments/assets/f3a9d15f-8763-4120-8356-9a1f73c88e85" /> <br/>

Next, We can add a unique ID to the filename somewhere, I use the file number from the SPT Hub but you are free to use anything you wish, it just has to be ONLY used with this or other versions of the same mod (this is the ID we will use for the Dependecy system to work). <br/>
<img width="381" height="33" alt="image" src="https://github.com/user-attachments/assets/f8b6b444-f8a5-4487-83c9-eccffd942b2b" />
<img width="757" height="43" alt="image" src="https://github.com/user-attachments/assets/01802bbe-d13e-4a71-a64d-9bf079cc193b" />

Lastly, This is where we will open the Archive and make changes to its layout, <br/>
 SVM asks that the "[SVM] Server Value Modifier" mod folder go into the 'user'/'mods' folder, <br/>
 <img width="225" height="38" alt="image" src="https://github.com/user-attachments/assets/67fdb699-af57-463b-be39-248a580423c8" />
 
In your workspace, Create 'user' Folder, Go inside, Create 'mods' Folder, Go inside and Extract SVM (or another mod with a similar issue), into that mods folder. <br/>
Go back 2 levels to your workspace area and package the 'user' folder into an archive, Either copy it into your fixed name download or make a new one (make sure the ID is the same) <br/>

<img width="1030" height="129" alt="image" src="https://github.com/user-attachments/assets/a75da892-805c-40fd-ad8f-ed2fe22bfb2e" />
The top level folder is now 'user' and we added 2 more folders to the archive.

And That's it! Use Vortex to install this mod and once you Activate it for your Profile and Deploy, you will see the SVM tool shortcut show up on your dashboard and in the Upper Left.
  </div>
</details>

---

<details open>
<summary>Creating Depencies, <sup> or Why I did all this work in the first place </sup> </summary>
  <div align="left">
Alright, Let's start making use of the powerful features of Vortex, Creating links between mods so that the program can keep track of which mods Require other mods, Must Load After (or Before), or Shouldn't be Deployed with each other. <br/> <br/>
    
Let's use Everyone's favorite AI overhaul mod. [SAIN - Solarint's AI Modifications - Full AI Combat System Replacement](https://hub.sp-tarkov.com/files/file/1062-sain-solarint-s-ai-modifications-full-ai-combat-system-replacement/) <br/>
    As you can see, Sain requires both [BigBrain](https://hub.sp-tarkov.com/files/file/1219-bigbrain/) and [Waypoints](https://hub.sp-tarkov.com/files/file/1119-waypoints-expanded-navmesh/). <br/>
    <sup> Because Solarint and DrakiaXYZ are GOATs, you only need to make filename changes to prep them for Vortex handling. </sup> <br/> <br/>
    Once installed, use the dependecy button to create links between SAIN, (Other versions of SAIN if you have them aswell), BigBrain, and Waypoints. <br/>
    Example of telling Vortex that SAIN 4.0.4 should not be loaded with other verions of SAIN (More specifically, It should not be loaded with ANY other mod that uses 1062 in its fild name)
    <img width="715" height="420" alt="image" src="https://github.com/user-attachments/assets/8d6854a4-1c89-4f41-a42e-4b3d37672882" /> <br/> <br/>
    When finished, you should see something similar to this, Notice how the links are made using the File ID we set earlier? That means if the mod auther changes the file name (hopefully to make vortex integration easier xP), the link will still work just fine.
    <img width="1819" height="406" alt="image" src="https://github.com/user-attachments/assets/dee55095-0704-4d55-9b13-1ba805aa73ac" /> <br/> <br/>
    Generally, I make 2 connections between mods,  <br/>
    1). "Requires": using the version match notation, (SAIN 4.0.4 requires at least Version 1.3.2 of Bigbrain) <br/>
    <img width="715" height="419" alt="image" src="https://github.com/user-attachments/assets/8dbc85ca-e0fb-4998-9f56-a3827970dbb3" /> <br/> <br/>
    2). "Must Load After": using any version notation, (SAIN 4.0.4 Must Deploy After ANY version of Bigbrain) <br/>
    <img width="697" height="391" alt="image" src="https://github.com/user-attachments/assets/ca7b2260-6e68-4d67-ac22-9b874f5e58e8" /> <br/> <br/>
    A great thing about having Vortex handle Dependency like this is that not only will it flag a warning that "Hey, some mod dependencies are not fulfilled"  <br/>
    <img width="509" height="71" alt="image" src="https://github.com/user-attachments/assets/5e0b4832-5e07-4abe-92bb-a248f89d3314" /> <br/> <br/>
    But it will also let you know that "Hey, The mod you enabled depends on other mods, do you want to enable those as well?" <br/>
    <img width="932" height="539" alt="image" src="https://github.com/user-attachments/assets/1fa4abe8-bfc4-4080-91d2-d3a1c9e9dbf5" /> <br/> <br/>
    The same for is true for the other direction, No longer using SAIN? Do you also want to diasble BigBrain and WAypoints now as well? (It even leaves them alone if something else you have enabled still requires them) <br/>
    <img width="940" height="544" alt="image" src="https://github.com/user-attachments/assets/66669b81-7ca5-4265-b843-9223b8204862" /> <br/>

  </div>
</details>

---
