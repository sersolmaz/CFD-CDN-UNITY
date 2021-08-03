using System.Collections;
using UnityEngine;

[AddComponentMenu("Localization/Localized Text")]
public class LocalizedTextAsset : MonoBehaviour
{
    public int
            index;

    public int langIntView;

    [SerializeField]
    private int setSize;

    // Use this for initialization
    private void Start ()
    {
        UpdateText();
    }

    private void Update ()
    {
        UpdateText();
    }

    private void UpdateText ()
    {
        if (GetComponent<GUIText>() != null)
        {
            GetComponent<GUIText>().text = LocalizeTools.GetLocalizedText(index);
        }
        if (GetComponent<TextMesh>() != null)
        {
            GetComponent<TextMesh>().text = LocalizeTools.GetLocalizedText(index);
        }
        if (GetComponent<UnityEngine.UI.Text>() != null)
        {
            GetComponent<UnityEngine.UI.Text>().text = LocalizeTools.GetLocalizedText(index);
        }
    }
}