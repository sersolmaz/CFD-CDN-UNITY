using System.Collections;
using UnityEngine;
using UnityEngine.UI;

public class newExampleGETTEXT : MonoBehaviour
{
    private Text text;

    public int rowToGet = 5;
    public bool withVariable = false;

    // Use this for initialization
    private void Start ()
    {
        text = GetComponent<Text>();
        text.text = LocalizeTools.GetLocalizedText(5);
    }

    // Update is called once per frame
    private void Update ()
    {
        //Insert the row that you would like to retrieve. It automatically assumes the language is the language currently set
        if (withVariable) text.text = LocalizeTools.GetLocalizedText(rowToGet) + " : " + Time.deltaTime.ToString();
        else text.text = LocalizeTools.GetLocalizedText(rowToGet);
    }
}