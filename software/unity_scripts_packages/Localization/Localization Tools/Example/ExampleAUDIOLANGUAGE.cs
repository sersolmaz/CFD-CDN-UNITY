using System.Collections;
using UnityEngine;

public class ExampleAUDIOLANGUAGE : MonoBehaviour
{
    private AudioSource source;
    public AudioClip[] clips;
    private int index = 0;

    // Use this for initialization
    private void Start ()
    {
        source = GetComponent<AudioSource>();
        index = LocalizeTools.LanguageInt - 1;
        source.clip = clips[index];
    }

    // Update is called once per frame
    private void Update ()
    {
        source = GetComponent<AudioSource>();
        index = LocalizeTools.LanguageInt - 1;
        if (index < clips.Length)
            if (clips[index] != null)
            {
                source.clip = clips[index];

                if (Input.GetKeyDown(KeyCode.Space))
                {
                    source.Play();
                }
            }
    }
}