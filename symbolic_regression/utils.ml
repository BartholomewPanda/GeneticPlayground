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

let uniform min max =
    let p = Random.float 1.0 in
    if p <= 0.5 then
        Random.float min
    else
        Random.float max

let load path =
    let regex = Str.regexp " +" in
    let file = open_in path in
    let stream =
        Stream.from (fun _ -> try Some (input_line file) with End_of_file -> None)
    in
    let result = ref [] in
    let f line =
        match Str.split regex line with
            | [x; y] -> result := (float_of_string x, float_of_string y) :: !result
            | _ -> ()
    in
    Stream.iter f stream;
    !result

