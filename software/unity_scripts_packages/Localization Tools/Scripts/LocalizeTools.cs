#if UNITY_EDITOR

using NPOI.HSSF.UserModel;
using NPOI.SS.UserModel;
using UnityEditor;

#endif

using System.Collections;
using System.IO;
using System.Linq;
using UnityEngine;

//Localization tool by http://namitentou.com

public class LocalizeTools : MonoBehaviour
{
    public static string filename = "/NAMI TENTOU/Localization Tools/Resources/localization.xls";

    private static TextAsset fileAsTextAsset;

    private static int languageInt = 1;

    public static string[,] grid;

    private static bool Initialized = true;

    public static int LanguageInt
    {
        get
        {
            if (grid == null) CreateLocalizationObject();
            return languageInt;
        }

        set
        {
            if (grid == null) CreateLocalizationObject();
            if (value < 1) value = 1;
            languageInt = value;
        }
    }

    public static int gridXLength
    {
        get
        {
            if (grid == null) CreateLocalizationObject();
            return grid.GetLength(0);
        }
    }

    public static void CreateLocalizationObject ()
    {
        grid = readXLS();
    }

    public static string[,] readXLS ()
    {
        string[,] returnedGrid = new string[0, 0];
        string name = filename;
        string fileCSV = "";

#if UNITY_EDITOR
        //Generates your temp file in case that you happen to have your XLS open at the same time
        FileUtil.DeleteFileOrDirectory(Application.dataPath + filename + "temp");

        if (!File.Exists(Application.dataPath + filename))
        {
            createNewFile();
        }

        FileUtil.CopyFileOrDirectory(Application.dataPath + filename, Application.dataPath + filename + "temp");

        using (FileStream stream = File.Open(Application.dataPath + filename + "temp", FileMode.Open, FileAccess.Read))
        {
            IWorkbook book = new HSSFWorkbook(stream);

            //Multiple Sheet Support? Maybe?
            ISheet sheet = book.GetSheetAt(0);
            int gridX = sheet.GetRow(0).LastCellNum;
            int gridY = sheet.LastRowNum + 1;

            returnedGrid = new string[gridX, gridY];

            for (int y = 0; y < gridY; y++)
            {
                IRow row = sheet.GetRow(y);

                for (int x = 0; x < gridX; x++)
                {
                    if (row == null) continue;
                    if (row.PhysicalNumberOfCells == 0) continue;

                    ICell cell = row.GetCell(x);
                    if (cell != null)
                    {
                        cell.SetCellType(CellType.String);
                        returnedGrid[x, y] = cell.StringCellValue;

                        //Replacing | with @p since that's our "comma" seperator
                        string tempCell = cell.StringCellValue.Replace("|", ",,,p");
                        //Replacing @ with @a since that's our new line seperator
                        tempCell = tempCell.Replace("@", ",,,a");

                        if (x + 1 != gridX) fileCSV += tempCell + "|";
                        else fileCSV += tempCell;
                    }
                    if (cell == null)
                    {
                        returnedGrid[x, y] = " ";
                        string tempCell = " ";

                        if (x + 1 != gridX) fileCSV += tempCell + "|";
                        else fileCSV += tempCell;
                    }
                }

                if (y + 1 != gridY) fileCSV += "@";
            }
            File.WriteAllText(Application.dataPath + "/NAMI TENTOU/Localization Tools/Resources/compiledbuild.txt", fileCSV);
        }

#endif
        if (Application.isPlaying)
        {
            TextAsset ta = Resources.Load("compiledbuild") as TextAsset;

            fileCSV = ta.text;
        }
        string[] tempGrid = fileCSV.Split('@');
        int width = tempGrid[0].Split('|').Length;
        int height = tempGrid.Length;

        returnedGrid = new string[width, height];

        for (int y = 0; y < height; y++)
        {
            string[] tempGrid2 = tempGrid[y].Split('|');
            for (int x = 0; x < tempGrid2.Length; x++)
            {
                string tempString = tempGrid2[x].Replace(",,,a", "@");
                tempString = tempString.Replace(",,,p", "|");

                returnedGrid[x, y] = tempString;
            }
        }

        return returnedGrid;
    }

    public static void createNewFile ()
    {
#if UNITY_EDITOR

        using (FileStream stream = File.Create(Application.dataPath + filename))
        {
            IWorkbook book = new HSSFWorkbook();

            //Multiple SHeet Support?
            ISheet sheet = book.CreateSheet();
            IRow row = sheet.CreateRow(0);
            ICell cell = row.CreateCell(0);
            cell.SetCellType(CellType.String);
            cell.SetCellValue(Application.productName + " Localization");

            ICell cell2 = row.CreateCell(1);
            cell2.SetCellType(CellType.String);
            cell2.SetCellValue("English");
            ICell cell3 = row.CreateCell(2);
            cell3.SetCellType(CellType.String);
            cell3.SetCellValue("French");
            ICell cell4 = row.CreateCell(3);
            cell4.SetCellType(CellType.String);
            cell4.SetCellValue("Italian");
            ICell cell5 = row.CreateCell(4);
            cell5.SetCellType(CellType.String);
            cell5.SetCellValue("German");
            ICell cell6 = row.CreateCell(5);
            cell6.SetCellType(CellType.String);
            cell6.SetCellValue("Spanish");

            IRow row2 = sheet.CreateRow(1);

            for (int i = 0; i < row.Cells.Count; i++)
            {
                ICell newCell = row2.CreateCell(i);
                newCell.SetCellType(CellType.String);
                newCell.SetCellValue(" ");
            }

            sheet.CreateRow(1);

            book.Write(stream);
        }
#endif
    }

    private static string[,] CrossPlatformReader (string s)
    {
        string[,] result;

        string[] arrayY = s.Split('@');
        int gridY = arrayY.Length;
        string[] arrayX = arrayY[0].Split('|');
        int gridX = arrayX.Length;

        result = new string[gridX, gridY];

        //This is reading our simple txt csv file so that the file can be read across multiple platforms
        for (int y = 0; y < gridY; y++)
        {
        }

        return result;
    }

    public static void writeToFile ()
    {
#if UNITY_EDITOR
        using (FileStream stream = File.Open(Application.dataPath + filename, FileMode.Open, FileAccess.Write))
        {
            IWorkbook book = new HSSFWorkbook();

            //Multiple SHeet Support?
            ISheet sheet = book.CreateSheet();
            int gridX = grid.GetLength(0);
            int gridY = grid.GetLength(1);

            for (int y = 0; y < gridY; y++)
            {
                IRow row = sheet.CreateRow(y);
                for (int x = 0; x < gridX; x++)
                {
                    ICell cell = row.CreateCell(x);

                    cell.SetCellType(CellType.String);
                    cell.SetCellValue(grid[x, y]);
                }
            }

            book.Write(stream);
        }

        readXLS();

#endif
    }

    public static void AddNewRow ()
    {
#if UNITY_EDITOR
        using (FileStream stream = File.Open(Application.dataPath + filename, FileMode.Open, FileAccess.Write))
        {
            IWorkbook book = new HSSFWorkbook();

            //Multiple SHeet Support?
            ISheet sheet = book.CreateSheet();
            int gridX = grid.GetLength(0);
            int gridY = grid.GetLength(1);

            for (int y = 0; y < gridY; y++)
            {
                IRow row = sheet.CreateRow(y);
                for (int x = 0; x < gridX; x++)
                {
                    ICell cell = row.CreateCell(x);

                    cell.SetCellType(CellType.String);
                    cell.SetCellValue(grid[x, y]);
                }
            }

            sheet.CreateRow(gridY);

            book.Write(stream);
        }

        readXLS();

#endif
    }

    public static int getColumnLength ()
    {
        if (grid == null) CreateLocalizationObject();
        if (grid.GetLength(1) == 0) return -1;
        return grid.GetLength(1) - 1;
    }

    /// <summary>
    /// Reads text from specific line from document
    /// </summary>
    public static string GetLocalizedText (int row)
    {
        if (row < 0) row = 0;

        string newString = "";
        if (grid == null) CreateLocalizationObject();

        if (row < grid.GetLength(1))
        {
            newString = grid[languageInt, row];
        }

        return newString;
    }

    /// <summary>
    /// Reads text from specific line from document while allowing you to manually specify language
    /// </summary>
    public static string GetLocalizedText (int langInt, int row)
    {
        if (row < 0) row = 0;

        string newString = "";
        if (grid == null) CreateLocalizationObject();
        if (row < grid.GetLength(0))
        {
            newString = grid[langInt, row];
        }
        return newString;
    }

    public static string GetLanguageName (int i)
    {
        return grid[i, 0];
    }
}