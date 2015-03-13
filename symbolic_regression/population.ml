(***********************************************************************)
(*                                                                     *)
(*                                OCaml                                *)
(*                                                                     *)
(*                   Bartholomew de La Villardière                     *)
(*                                                                     *)
(*                     http://www.bartholomew.fr/                      *)
(*                https://github.com/BartholomewPanda                  *)
(*                                                                     *)
(***********************************************************************)

type t = {genome: Chromosome.t array; size: int}

let create f size =
    let genome = Array.init size f in
    {genome; size}

(* compute the next generation (with elitism) *)
let next breeding p =
    let rec make i new_p =
        if i + 1 >= p.size then
            new_p
        else
            let father = p.genome.(i) in
            let mother = p.genome.(i + 1) in
            let o1, o2 = breeding father mother in
            make (i + 2) (o1 :: o2 :: new_p)
    in
    Array.sort Chromosome.cmp p.genome;
    {genome = Array.of_list (p.genome.(0) :: (make 0 [])); size = p.size}

let debug_display fitness display p =
    Array.sort Chromosome.cmp p.genome;
    let best = p.genome.(0) in
    let worst = p.genome.(p.size - 1) in
    (*Printf.printf "%d;%f;%f\n" i best.fitness w.fitness;*)
    Chromosome.debug_display best;
    Chromosome.debug_display worst

