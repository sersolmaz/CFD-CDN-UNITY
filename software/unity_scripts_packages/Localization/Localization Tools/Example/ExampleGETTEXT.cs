using System.Collections;
using UnityEngine;

public class ExampleGETTEXT : MonoBehaviour
{
    private TextMesh textMesh;

    public int rowToGet = 5;
    public bool withVariable = false;

    // Use this for initialization
    private void Start ()
    {
        textMesh = GetComponent<TextMesh>();
        textMesh.text = LocalizeTools.GetLocalizedText(5);
    }

    // Update is called once per frame
    private void Update ()
    {
        //Insert the row that you would like to retrieve. It automatically assumes the language is the language currently set
        if (withVariable) textMesh.text = LocalizeTools.GetLocalizedText(rowToGet) + " : " + Time.deltaTime.ToString();
        else textMesh.text = LocalizeTools.GetLocalizedText(rowToGet);
    }
}