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

type t = {genes: float array; mutable fitness: float}

(* create a new chromosome *)
let create fitness min max =
    let genes = Array.init 6 (fun _ -> Utils.uniform max min) in
    let chromosome = {genes; fitness = 0.0} in
    fitness chromosome;
    chromosome

(* copy one chromosome *)
let copy c =
    {genes = Array.copy c.genes; fitness = c.fitness}

(* used to compare two chromosomes *)
let cmp c1 c2 =
    if c1.fitness > c2.fitness then 1
    else if c2.fitness > c1.fitness then -1
    else 0

(*
 * simple mutation of a chromosomes
 * mr: mutation rate
 *)
let mutation mr c =
    let i = Random.int 6 in
    let d = abs_float (0.00001 *. c.genes.(i)) in
    c.genes.(i) <- c.genes.(i) +. (Utils.uniform (-1.0 *. d) d)

(* Wright's crossover *)
let crossover fitness c1 c2 =
    let o = [|copy c1; copy c2; copy c1|] in
    for i = 0 to 5 do
        o.(0).genes.(i) <- 0.5 *. c1.genes.(i) +. 0.5 *. c2.genes.(i);
        o.(1).genes.(i) <- 1.5 *. c1.genes.(i) -. 0.5 *. c2.genes.(i);
        o.(2).genes.(i) <- (-0.5) *. c1.genes.(i) +. 1.5 *. c2.genes.(i)
    done;
    Array.iter fitness o;
    Array.sort cmp o;
    (o.(0), o.(1))

(*
 * breeding of two chromosomes
 * pc: probability of crossover
 * pm: probability of mutation
 *)
let breeding fitness mutation pc pm c1 c2 =
    let o1, o2 =
        if Random.float 1.0 < pc then crossover fitness c1 c2
        else (c1, c2)
    in
    if Random.float 1.0 < pm then
        mutation o1;
    if Random.float 1.0 < pm then
        mutation o2;
    (o1, o2)

(* compute the fitness of a chromosome *)
let fitness f values c =
    let error result (x, y) =
        let r = y -. (f c.genes x) in
        result +. (r *. r)
    in
    c.fitness <- sqrt (List.fold_left error 0.0 values)

let debug_display c =
    Printf.printf "%f\t-->\t[" c.fitness;
    Array.iter (Printf.printf "%.15f;") c.genes;
    Printf.printf "]\n"

