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

(* ==== CONFIGURATION ==== *)
let population_size = 500
let min_chromosome = (-1000.0)
let max_chromosome = 1000.0
(* probability of crossover *)
let pc = 0.85
(* probability of mutation *)
let pm = 0.0001
(* mutation rate *)
let mr = 0.00001
let nb_turn = 3000
(* ======================= *)


(* function *)
let f chromosome x =
    chromosome.(0) +.
    chromosome.(1) *. x +.
    chromosome.(2) *. (x *. x) +.
    chromosome.(3) *. (x *. x *. x) +.
    chromosome.(4) *. (x *. x *. x *. x) +.
    chromosome.(5) *. (x *. x *. x *. x *. x)


let fitness = Chromosome.fitness f (Utils.load "./datfile.dat")
let create _ = Chromosome.create fitness min_chromosome max_chromosome
let mutation = Chromosome.mutation mr
let breeding = Chromosome.breeding fitness mutation pc pm
let next = Population.next breeding


let rec run acc p =
    Printf.printf "===step:%d===\n" acc;
    Array.sort Chromosome.cmp p.Population.genome;
    Chromosome.debug_display p.Population.genome.(0);
    Printf.printf "=============\n";
    flush stdout;
    if acc >= nb_turn then
        p
    else
        run (acc + 1) (next p)


let _ =
    Random.self_init ();
    let p = Population.create create population_size in
    run 1 p

