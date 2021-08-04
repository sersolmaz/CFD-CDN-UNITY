using System.Collections;
using UnityEngine;

public class ExampleCHANGELANGUAGE : MonoBehaviour
{
    public int language = 2;

    // Use this for initialization
    private void Start ()
    {

    }

    // Update is called once per frame
    private void Update ()
    {
        if (Input.GetKeyDown(KeyCode.LeftArrow)) language--;

        if (Input.GetKeyDown(KeyCode.RightArrow)) language++;

        language = Mathf.Clamp(language, 0, LocalizeTools.gridXLength - 1);

        //Below is the command you use to set the language to what you want. Useful for options in game.
        LocalizeTools.LanguageInt = (language);
    }
}