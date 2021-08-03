using System.Collections;
using UnityEditor;
using UnityEngine;

[InitializeOnLoad]
public class LocalizationMenu
{
    static LocalizationMenu ()
    {
        LocalizeTools.CreateLocalizationObject();
    }

    //[MenuItem("Localization/Open Localization XLS File")]
    //private static void OpenFile ()
    //{
    //    EditorUtility.OpenWithDefaultApp(Application.dataPath + LocalizeTools.filename);
    //}

    [MenuItem("Localization/Import XLS File")]
    private static void ImportFile ()
    {
        string path = EditorUtility.OpenFilePanel("Import Localization XLS File", "", "xls");

        if (string.IsNullOrEmpty(path)) return;

        FileUtil.DeleteFileOrDirectory(Application.dataPath + LocalizeTools.filename);
        FileUtil.CopyFileOrDirectory(path, Application.dataPath + LocalizeTools.filename);

        LocalizeTools.readXLS();
    }

    [MenuItem("Localization/Export XLS File")]
    private static void ExportFile ()
    {
        string path = EditorUtility.SaveFilePanel("Export Localization XLS File", "", Application.productName + " Localization " + System.DateTime.Now.ToString("yyyy-MM-dd HH_mm_ss") + ".xls", "xls");

        if (string.IsNullOrEmpty(path)) return;

        FileUtil.ReplaceFile(Application.dataPath + LocalizeTools.filename, path);

        LocalizeTools.readXLS();
    }

    [MenuItem("Localization/Refresh Cache")]
    private static void GenerateFile ()
    {
        LocalizeTools.readXLS();
    }
}