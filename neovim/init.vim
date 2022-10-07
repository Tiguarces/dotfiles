
    " ---------------------------------------------
    " ----------- S O U R C E S ----------------       
    " --------------------------------------
    
    source $HOME/.config/nvim/keybirdings.vim
    source $HOME/.config/nvim/coc.vim
    source $HOME/.config/nvim/plugins.vim
    source $HOME/.config/nvim/plugins/rnvimr/rnvimr.vim


    " ---------------------------------------------
    " ----------- B A S E   C O N F I G --------       
    " --------------------------------------

    " Split
    set splitright
    set splitbelow

    " Font
    set guifont=Monoid-Italic\ Nerd\ Font\ 11

    " FileType
    filetype plugin on

    " Theme
    if (has("nvim"))
      let $NVIM_TUI_ENABLE_TRUE_COLOR=1
    endif

    if (has("termguicolors"))
     set termguicolors
    endif

    syntax enable
    set termguicolors
 
    let g:oceanic_italic_comments = 1
    let g:oceanic_for_polyglot = 1
    colorscheme oceanicnext

    " Number lines
    set nu

    " Syntax
    syntax enable

    " Indenting
    set tabstop=4
    set shiftwidth=4
    set expandtab
    set linebreak

    " Dev Icons
    let g:webdevicons_enable = 1
    let g:webdevicons_enable_nerdtree = 1

    " Startify
    let g:startify_custom_header =
       \ startify#pad(split(system('figlet -f big -k -c -w 100 Lonux'), '\n'))

