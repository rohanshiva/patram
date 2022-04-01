# Styling

## Themes
You can easily customize different themes for patram by interacting with these CSS variables. `:root` tag defines colors for light mode, and `[data-theme="dark"]` tag defines colors for dark mode.

- `bg`: background color 
- `primary` : primary text color 
- `secondary`:   secondary color used for link <a></a> content
- `accent`:  used for scroll bar, selected links (page titles),  
- `content`:   color for page content 
- `hover-highlight`:   page-title color on hover 
- `code-bg`:  code block bg color 
- `code-color`:  code block content color 
- `logo-bg`:   logo bg color 
- `logo-text`:   logo content color 

Default theme CSS:

```css
    :root {
      --bg: #fffefe; /* background color */
      --primary: black; /* primary text color */
      --secondary: #7c7d80; /* secondary color used for link <a></a> content */
      --accent: #0068ff; /* used for scroll bar, selected links (page titles), */ 
      --content: black; /* color for page content */
      --hover-highlight: #f4f4f6; /* page-title color on hover */
      --code-bg: #f6f8fa; /* code block bg color */
      --code-color: black; /* code block content color */
      /* Logo Colors */
      --logo-bg: #131415; /* logo bg color */
      --logo-text: #fffefe; /* logo content color */
    }

    [data-theme="dark"] {
      --bg: #131415;
      --primary: white;
      --secondary: #b1b6be;
      --accent: #ff7c7c;
      --content: white;
      --hover-highlight: #ff7c7c38;
      --code-bg: #292d3e;
      --code-color: white;
      /* Logo Colors */
      --logo-bg: white;
      --logo-text: #ff2e2e;
    }
```

## Tags

### `inline-code`:
- For inline code snippets like this `hello!`

### `highlight`: 
- When page title on sidebar is selected.

### `page-title`:
- Page title on the sidebar.

### `dir-title`:
- Directory/folder name on the sidebar

### `title`:
- Website title **Patram** in this case.

### `sidebar`:
- Sidebar layout styling.

### `menu-buttons`:
- Styling for menu buttons in the sidebar (includes open/close, dark/light mode toggle)

### `open-button`:
- Open button used to open list of pages in smaller screens.

### `close-button`:
- Close button used to close list of pages in smaller screens.

### `theme-button`:
- Toggle dark/light mode.

### `content`:
- Layout for markdown page content. 