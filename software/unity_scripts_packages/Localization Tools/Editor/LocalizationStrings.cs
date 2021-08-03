using System.Collections;
using UnityEditor;
using UnityEngine;

public class LocalizationStrings : EditorWindow
{
    private bool changesToSave = false;
    public Rect windowRect = new Rect(20, 20, 120, 50);
    private Vector2 scrollPos;

    [MenuItem("Localization/Strings Editor")]
    private static void OpenEditStringsWindow ()
    {
        GetWindow(typeof(LocalizationStrings), false, "Localization");
    }

    private void OnGUI ()
    {
        EditorGUILayout.BeginHorizontal();

        for (int i = 0; i < LocalizeTools.grid.GetLength(0); i++)
        {
            EditorGUILayout.LabelField(LocalizeTools.GetLanguageName(i));
        }

        EditorGUILayout.EndHorizontal();
        EditorGUI.BeginChangeCheck();
        scrollPos = EditorGUILayout.BeginScrollView(scrollPos);
        for (int y = 1; y < LocalizeTools.grid.GetLength(1); y++)
        {
            EditorGUILayout.BeginHorizontal();
            for (int x = 0; x < LocalizeTools.grid.GetLength(0); x++)
            {
                string result = EditorGUILayout.TextField(LocalizeTools.grid[x, y]);
                LocalizeTools.grid[x, y] = result;
            }
            EditorGUILayout.EndHorizontal();
        }
        EditorGUILayout.EndScrollView();
        if (EditorGUI.EndChangeCheck()) changesToSave = true;

        GUILayout.BeginHorizontal();
        if (GUILayout.Button("Save")) { LocalizeTools.writeToFile(); changesToSave = false; }
        if (GUILayout.Button("Reload")) { LocalizeTools.CreateLocalizationObject(); changesToSave = false; }
        if (GUILayout.Button("Add New Row"))
        {
            LocalizeTools.AddNewRow();
            LocalizeTools.CreateLocalizationObject();
        }

        if (GUILayout.Button("Create New File")) if (EditorUtility.DisplayDialog("Create a new file?", "This will delete your current file. Are you sure?", "Yeah, delete my hard work.", "Cancel")) { LocalizeTools.createNewFile(); LocalizeTools.CreateLocalizationObject(); changesToSave = false; }

        GUILayout.EndHorizontal();

        if (changesToSave)
            EditorGUILayout.LabelField("There are changes to save!");
        else
            EditorGUILayout.LabelField("Up to date.");
    }

    private void OnValidate ()
    {
    }
}