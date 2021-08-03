using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;
using System.Text.RegularExpressions;

public class ToTextFile : MonoBehaviour
{
    public InputField inputFieldChat;

    void Start()
    {
        Directory.CreateDirectory(Application.streamingAssetsPath + "/Chat_Logs/");

    }

    
    public void CreateTexFile()
    {

        //assume there already script in the text file
        if(inputFieldChat.text == "")
        {
            return;
        }
        
        string txtDocumentName = Application.streamingAssetsPath + "/Chat_Logs/" + "Chat" + ".txt";

        if (!File.Exists(txtDocumentName))
        {
            File.WriteAllText(txtDocumentName, "TITLE OF MY CHAT LOG \n\n");
        }

        File.AppendAllText(txtDocumentName, "\n");
        //File.AppendAllText(txtDocumentName, inputFieldChat.text + "\n");

        int line_to_edit = 31;
        string newText = "        " + "omega" + "         " + inputFieldChat.text + ";";
        string[] arrLine = File.ReadAllLines(txtDocumentName);
        arrLine[line_to_edit - 1] = newText;
        File.WriteAllLines(txtDocumentName, arrLine);

        //clear input field
        //inputFieldChat.text = "";

    }


}

