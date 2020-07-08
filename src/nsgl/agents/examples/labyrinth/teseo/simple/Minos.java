package nsgl.agents.examples.labyrinth.teseo.simple;

import nsgl.agents.simulate.util.SimpleLanguage;

import java.util.*;

public class Minos extends SimpleTeseoAgentProgram {
    protected String px = "0";
    protected String py = "0";
    protected String dir = "N";
    protected Set<String> Memory = new HashSet<>();
    protected Stack<String> Options = new Stack<>();

    public Minos() {
        px = "0";
        py = "0";
        dir = "N";
        Memory.add(px+":"+py);
        Options.push(px+":"+py+":"+dir);
    }

    public Minos(   SimpleLanguage _language  ) {
        super(_language);
    }

    @Override
    public int accion(boolean PF, boolean PD, boolean PA, boolean PI, boolean MT, boolean FAIL) {
        /*
        -1 = Goal, MT=True
        0 = Rotate 0, PF=False
        1 = Rotate 1, PD=False
        2 = Rotate 2, PA=False
        3 = Rotate 3, PI=False
        */
        if (MT) return -1;
        boolean flag = false;
        int action = 0;
        if(!PF) {
            if (dir.equals("N")) {
                py = Integer.toString(Integer.parseInt(py) + 1);
                if(!Memory.contains(px + ":" + py)) {
                    Memory.add(px + ":" + py);
                    Options.push(px + ":" + py + ":" + dir);
                    flag = true;
                }
            }else if(dir.equals("S")){
                py = Integer.toString(Integer.parseInt(py) - 1);
                if(!Memory.contains(px + ":" + py)) {
                    Memory.add(px + ":" + py);
                    Options.push(px + ":" + py + ":" + dir);
                    flag = true;
                }
            }else if(dir.equals("E")){
                px = Integer.toString(Integer.parseInt(px) + 1);
                if(!Memory.contains(px + ":" + py)) {
                    Memory.add(px + ":" + py);
                    Options.push(px + ":" + py + ":" + dir);
                    flag = true;
                }
            }else if(dir.equals("W")){
                px = Integer.toString(Integer.parseInt(px) - 1);
                if(!Memory.contains(px + ":" + py)) {
                    Memory.add(px + ":" + py);
                    Options.push(px + ":" + py + ":" + dir);
                    flag = true;
                }
            }
            if(!flag){
                String[] data = Options.pop().split(":");
                
            }

        }else if(!PD) {
            if (dir.equals("N")) {
                px = Integer.toString(Integer.parseInt(py) + 1);
                Memory.add(px + ":" + py);
                Options.push(px + ":" + py + ":" + "E");
            }else if(dir.equals("S")){
                px = Integer.toString(Integer.parseInt(py) - 1);
                Memory.add(px + ":" + py);
                Options.push(px + ":" + py + ":" + "W");
            }else if(dir.equals("E")){
                py = Integer.toString(Integer.parseInt(px) - 1);
                Memory.add(px + ":" + py);
                Options.push(px + ":" + py + ":" + "S");
            }else if(dir.equals("W")){
                py = Integer.toString(Integer.parseInt(px) + 1);
                Memory.add(px + ":" + py);
                Options.push(px + ":" + py + ":" + "N");
            }
            action = 1;
        }else if(!PI) {
            if (dir.equals("N")) {
                px = Integer.toString(Integer.parseInt(py) - 1);
                Memory.add(px + ":" + py);
                Options.push(px + ":" + py + ":" + "W");
            }else if(dir.equals("S")){
                px = Integer.toString(Integer.parseInt(py) + 1);
                Memory.add(px + ":" + py);
                Options.push(px + ":" + py + ":" + "E");
            }else if(dir.equals("E")){
                py = Integer.toString(Integer.parseInt(px) + 1);
                Memory.add(px + ":" + py);
                Options.push(px + ":" + py + ":" + "N");
            }else if(dir.equals("W")){
                py = Integer.toString(Integer.parseInt(px) - 1);
                Memory.add(px + ":" + py);
                Options.push(px + ":" + py + ":" + "S");
            }
            action = 3;
        }else{
            String[] data = Options.pop().split(":");
            action = 2;
        }

        return action;
    }
}
