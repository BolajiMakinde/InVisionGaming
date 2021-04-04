using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.IO;

public class Haptics : MonoBehaviour
{
    [SerializeField]
    public List<GameObject> AllSensors = new List<GameObject>();
    [SerializeField]
    public List<int> AllSensorXs = new List<int>();
    [SerializeField]
    public List<int> AllSensorYs = new List<int>();
    public Ball[,] BGA = new Ball[24,24];
    public bool updateBGA = false;
    public string BGAStatePath = "";
    // Start is called before the first frame update
    void Start()
    {
        foreach(GameObject go in GameObject.FindObjectsOfType(typeof(GameObject)))
        {
            if(go.name.Length > 5 && go.name.Substring(0,6) == "Sphere") {
                AllSensors.Add (go);
                if(!AllSensorXs.Contains((int)Math.Round(go.transform.position.x))) {
                    AllSensorXs.Add((int)Math.Round(go.transform.position.x));
                }
                if(!AllSensorYs.Contains((int)Math.Round(go.transform.position.z))) {
                    AllSensorYs.Add((int)Math.Round(go.transform.position.z));
                }
            }
        }
        AllSensorXs.Sort();
        AllSensorYs.Sort();
        print (AllSensors.Count);
        print (AllSensorXs.Count);
        print(AllSensorYs.Count);

        foreach(GameObject Sensor in AllSensors)
        {
            Ball b = Sensor.AddComponent(typeof(Ball)) as Ball;
            for(int i = 0; i < AllSensorXs.Count; i++) {
                if((int)Math.Round(Sensor.transform.position.x) == AllSensorXs[i])
                {
                    b.x = i;
                }
            }
            for(int i = 0; i < AllSensorYs.Count; i++) {
                if((int)Math.Round(Sensor.transform.position.z) == AllSensorYs[i])
                {
                    b.y = i;
                }
            }
            BGA[b.x,b.y] = b;
        }
         

    }

    // Update is called once per frame
    void Update()
    {
        if(updateBGA == true) {

            System.IO.StreamReader file = new System.IO.StreamReader(BGAStatePath);
            int i = 0;
            string line;
            while((line = file.ReadLine()) != null)  
            {
                int j = 0;
                foreach(char c in line)
                {
                    BGA[i,j].UpdateLevel((int)Char.GetNumericValue(c));
                    j++;
                }
                i++;
            }
            file.Close();
        }
    }
}
