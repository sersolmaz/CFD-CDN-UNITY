using System.Collections;
using UnityEditor;
using UnityEngine;

[CustomEditor(typeof(LocalizedTextAsset))]
public class ReadTextEditor : Editor
{
    private string[,] grid;
    private string textToDisplay;
    private string[] displayStrings;
    private int languageInt = 0;
    private int length;
    private string[] Options;
    private int[] lValues;
    private LocalizedTextAsset myText;

    private void OnEnable ()
    {
        LocalizeTools.CreateLocalizationObject();
        grid = LocalizeTools.grid;

        length = grid.GetLength(0);

        Options = new string[length];
        lValues = new int[length];

        for (int i = 1; i < length; i++)
        {
            Options[i] = LocalizeTools.GetLanguageName(i);
            lValues[i] = i;
        }
    }

    public override void OnInspectorGUI ()
    {
        myText = (LocalizedTextAsset)target;

        myText.langIntView = EditorGUILayout.IntPopup(myText.langIntView, Options, lValues);
        languageInt = myText.langIntView;

        EditorGUILayout.BeginHorizontal();
        if (GUILayout.Button("<")) myText.index--;

        myText.index = (EditorGUILayout.IntField("Row", myText.index + 1)) - 1;

        if (GUILayout.Button(">")) myText.index++;

        if (myText.index <= 0)
        {
            myText.index = 1;
        }

        EditorGUILayout.EndHorizontal();

        if (myText.index <= LocalizeTools.getColumnLength()) textToDisplay = grid[languageInt, myText.index];
        else { AddNewRowButton(); return; }

        EditorGUI.BeginChangeCheck();
        grid[languageInt, myText.index] = EditorGUILayout.TextField("Localization Text", textToDisplay, GUILayout.Height(80));
        grid[0, myText.index] = EditorGUILayout.TextField("Notes", grid[0, myText.index], GUILayout.Height(80));

        if (EditorGUI.EndChangeCheck())
        {
            LocalizeTools.writeToFile();
            Debug.Log("saving");
        }

        if (Selection.activeGameObject.GetComponent<TextMesh>() != null)
            Selection.activeGameObject.GetComponent<TextMesh>().text = grid[languageInt, myText.index];

        if (Selection.activeGameObject.GetComponent<GUIText>() != null)
            Selection.activeGameObject.GetComponent<GUIText>().text = grid[languageInt, myText.index];

        if (Selection.activeGameObject.GetComponent<UnityEngine.UI.Text>() != null)
            Selection.activeGameObject.GetComponent<UnityEngine.UI.Text>().text = grid[languageInt, myText.index];

        if (GUILayout.Button("Save"))
        {
            LocalizeTools.writeToFile();
            Debug.Log("Saved localization data to file: " + LocalizeTools.filename);
        }

        AddNewRowButton();

        if (GUILayout.Button("Reload"))
        {
            LocalizeTools.CreateLocalizationObject();
            grid = LocalizeTools.grid;
            length = grid.GetLength(0);

            Options = new string[length];
            lValues = new int[length];

            for (int i = 1; i < length; i++)
            {
                Options[i] = LocalizeTools.GetLanguageName(i);
                lValues[i] = i;
            }

            Debug.Log("Loaded localization data from file: " + LocalizeTools.filename);
        }
    }

    private void AddNewRowButton ()
    {
        if (GUILayout.Button("Add New Row"))
        {
            LocalizeTools.AddNewRow();
            LocalizeTools.CreateLocalizationObject();
            grid = LocalizeTools.grid;
            length = grid.GetLength(0);

            Options = new string[length];
            lValues = new int[length];

            for (int i = 1; i < length; i++)
            {
                Options[i] = LocalizeTools.GetLanguageName(i);
                lValues[i] = i;
            }

            myText.index = LocalizeTools.getColumnLength();
        }
    }
}