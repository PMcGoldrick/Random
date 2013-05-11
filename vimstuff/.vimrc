let pymode_rope_extended_complete=1
let g:pymode_rope = 1
autocmd FileType python set omnifunc=pythoncomplete#Complete
call pathogen#infect()
call pathogen#helptags()
colorscheme koehler
filetype plugin indent on
syntax on
set hidden
