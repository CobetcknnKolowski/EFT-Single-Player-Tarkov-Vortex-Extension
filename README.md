# EFT-Single-Player-Tarkov-Vortex-Extension
This is an Extension for the Vortex Modding platform Created by Nexus Mods that allows you to use Vortex to manage your Single Player Tarkov mods.

Please Pardon the mess, This is all new to me from the Developer side.
---
<details>
<summary>Installing/Updating the extension </summary>
  <div align="left">
    Go to the "Extensions" List in the Vortex app <br/>   
    <img align="left" width="238" height="410" alt="image" src="https://github.com/user-attachments/assets/1415c11c-7e1a-411f-a295-4d017e8e7b37" /> <br/> 
    Click on the button in the bottom right and select the zip file you downloaded, "Vortex Extension Update - Escape From Tarkov - Single Player Tarkov Mod Vortex Extension Vx.x.x". <br/> 
    <img width="1297" height="155" alt="image" src="https://github.com/user-attachments/assets/f973fea5-ee8e-45d0-a0e7-357024a621ae" /> <br/> 
    Restart Vortex, and Search the "Extensions" List, if you see it, it successfuly installed, If not, Repeat install and restart. (I do not know why Multiple install attempts is needed sometimes) <br/> 
    <img width="612" height="187" alt="image" src="https://github.com/user-attachments/assets/193c7021-bb59-4ee2-8862-dfe9097e0e09" /> <br/> 
    Go to the "Games" tab <br/> 
    <img width="259" height="544" alt="image" src="https://github.com/user-attachments/assets/f871b75a-c84b-4b9c-9788-c9c68a31dc0b" /> <br/> 
    Search for "Tarkov" <br/>
    <img width="330" height="195" alt="image" src="https://github.com/user-attachments/assets/51401b8b-102c-43c7-889b-ea5a358feaba" /> <br/> 
    Click on it to Activate and it should ask you where you have SPT installed, (Where are SPT.Server.exe and SPT.Launcher located). <br/> 
    Congrats, Vortex can now handle your mod installs as well as activating or deactivating mods. <br/> 
    To see where Vortex is downloading and staging your mods, go to the "Settings" List and check the "Mods" and "Download" Tabs, you can also change the paths for both if you have somewhere else you'd rather mods be stored. <br/> 
    <img width="1027" height="587" alt="image" src="https://github.com/user-attachments/assets/01885f83-763a-4b93-ac4f-8cd88f4e87b6" /> <br/>
  </div>
</details>

---
 
<details>
<summary>Supported Tools</summary>
  <div align="left">
    Vortex allows you to create shortcuts to tools that can easily be accessed from your Vortex dashboard <br/> 
    Included in the extension is the "SPT Server" and "SPT Launcher" exe's as well as the foundation for other popular Mod tools made by the community <br/> 
    1. Server Value Manager, https://hub.sp-tarkov.com/files/file/379-server-value-modifier-svm/ <br/> 
    2. Load Order Editor Drag'n'Drop, https://hub.sp-tarkov.com/files/file/1923-load-order-editor-drag-drop/ <br/> 
    3. LOE - Load Order Editor, https://hub.sp-tarkov.com/files/file/1082-loe-load-order-editor/ <br/> 
    4. Acid's Bot Placement System, https://hub.sp-tarkov.com/files/file/2782-abps-acid-s-bot-placement-system/ <br/> <br/>
    
   **You will still need to download and install any of the above mods you wish to use into their expected (default) locations, I merely laid the basic file structure and pointers so that Vortex will instantly recognize and populate the shortcuts. Yes having Vortex handle the install is fine, in fact you should let Vortex handle as many of the installations as possible.**
  </div>
</details>

---

<details>
<summary>Installing Mods</summary>
    <div align="left">
Unfortunately, It is not completely hands off endeavour if you want to take advantage of all the features of Vortex: Proper Deployment, Dependencies and the Variants systems. <br/><br/>

First, We will need to make sure that the mod is packaged as Vortex expects. Let's use Server Value Modifier as an example that requires manual intervention, (apologies for putting you on blast GhostFenixx xP)
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

And That's it, Ask Vortex to install this mod and once you activate it, you will see the SVM tool popup on your dashboard in the Upper Left.
  </div>
</details>


List of mods that require user interventure
