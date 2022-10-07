    " Ale
    let g:ale_disable_lsp = 1
    let g:ale_set_quickfix = 1
    let g:streamline_show_ale_status = 1

    " Plugins
    call plug#begin("~/.config/nvim/plugins")

        "Auto pairs for '(' '[' '{'
        Plug 'jiangmiao/auto-pairs'

        " Theme
        Plug 'morhetz/gruvbox'
        Plug 'mhartington/oceanic-next'

        " Dev icons
        Plug 'ryanoasis/vim-devicons'

        " CSS color
        Plug 'ap/vim-css-color'

        " Welcome screen
        Plug 'mhinz/vim-startify'

        " Auto close tag
        Plug 'alvan/vim-closetag'

        "Coc 
        Plug 'neoclide/coc.nvim', {'branch': 'release'}

        " Tabs
        Plug 'pacha/vem-tabline'

        " NerdTree plugin
        Plug 'tiagofumo/vim-nerdtree-syntax-highlight'

        " Ranger
        Plug 'kevinhwang91/rnvimr'

        " Color picker
        Plug 'KabbAmine/vCoolor.vim'

        " Streamline
        Plug 'KaraMCC/vim-streamline'

        " Oceanic theme
        Plug 'mhartington/oceanic-next'

        " Oceanic Material theme
        Plug 'glepnir/oceanic-material'

        " Oceanic theme v2
        Plug 'adrian5/oceanic-next-vim'

        " Polygot 
        Plug 'sheerun/vim-polyglot'

        " Ale
        Plug 'dense-analysis/ale'
        
        " Rigel theme
        Plug 'Rigellute/rigel'

    call plug#end()
