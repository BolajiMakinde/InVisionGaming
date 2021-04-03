using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Ball : MonoBehaviour
{

    public int level = 1;

    public int x = -1;

    public int y = -1;

    public Vector3 globalPos = new Vector3(-1.0f,-1.0f,-1.0f);

    // Start is called before the first frame update
    void Start()
    {
        globalPos.x = transform.position.x;
        globalPos.y = transform.position.y;
        globalPos.z = transform.position.z;
    }

    void UpdateLevel(int newLevel)
    {
        level = newLevel;
        if(level == 0){
            gameObject.transform.localPosition = new Vector3(gameObject.transform.localPosition.x, -0.0127f, gameObject.transform.localPosition.z);
        }
        else if(level == 1)
        {
            gameObject.transform.localPosition = new Vector3(gameObject.transform.localPosition.x, 0f, gameObject.transform.localPosition.z);;
        }
        else{
            gameObject.transform.localPosition  = new Vector3(gameObject.transform.localPosition.x, -0.21f, gameObject.transform.localPosition.z);;
        }
    }
}
