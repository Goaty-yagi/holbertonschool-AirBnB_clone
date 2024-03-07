# Learning Objectives

- [What is HTML](#What-is-HTML)
- [How to create an HTML page](#How-to-create-an-HTML-page)
- [What is a markup language](#What-is-a-markup-language)
- [What is the DOM](#What-is-the-DOM)
- [What is an element / tag](#What-is-an-element-/-tag)
- [What is an attribute](#What-is-an-attribute)
- [How does the browser load a webpage](#How-does-the-browser-load-a-webpage)
- [What is CSS](#What-is-CSS)
- [How to add style to an element](#How-to-add-style-to-an-element)
- [What is a class](#What-is-a-class)
- [What is a selector](#What-is-a-selector)
- [How to compute CSS Specificity Value](#How-to-compute-CSS-Specificity-Value)
- [What are Box properties in CSS](#What-are-Box-properties-in-CSS)

## What is HTML
HyperText Markup Language, is the standard markup language used to create and design documents on the World Wide Web.
## How to create an HTML page
in index.html file
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First HTML Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>

```
## What is a markup language
Markup languages use tags and attributes to convey instructions for document processing or presentation without directly affecting the document's appearance.

### Exapmles
- HTML
- XML
- Markdown

## What is the DOM
Document Object Model, is a programming interface for web documents. It represents the structure of a document as a tree of objects.
The DOM represents an HTML or XML document as a tree structure, where each node in the tree corresponds to an element, attribute, or other part of the document.

## What is an element / tag
### Tag
- Start Tag <p>
- Content "Something"
- End Tag </p>

### Element
- <p>Something</p>

## What is an attribute
<a href="https://www.example.com">Visit Example</a>

href is attribute

## How does the browser load a webpage

### User Input or Request:

- The process begins when a user enters a URL (Uniform Resource Locator) in the browser's address bar or clicks on a hyperlink.

### DNS Resolution:
- The browser sends a Domain Name System (DNS) request to resolve the entered domain name into an IP address. DNS translates human-readable domain names (e.g., www.example.com) into machine-readable IP addresses.

### HTTP Request:
- Once the IP address is obtained, the browser makes an HTTP (Hypertext Transfer Protocol) request to the web server associated with that IP address. The request includes the specific resource (webpage, image, stylesheet, etc.) the browser is requesting.

### Server Processing:
- The web server processes the request and retrieves the requested resource. If it's an HTML document, the server may also fetch additional resources referenced in the HTML, such as stylesheets, scripts, and images.

### Response from Server:
- The server responds to the browser's request with the requested resource. The response includes the status of the request (e.g., success or error) and the content of the resource.

### HTML Parsing:

- The browser begins parsing the received HTML document. It creates a Document Object Model (DOM) tree, which represents the structure of the HTML document. The browser identifies and parses linked resources, such as stylesheets and scripts.

### CSS and JavaScript Processing:
- If the HTML document references external stylesheets, the browser fetches and applies them to the DOM, enhancing the visual presentation. JavaScript files are also fetched and executed, adding interactivity and dynamic behavior to the webpage.

### Rendering:
- The browser combines the DOM, CSS, and JavaScript to create the final rendered page. This involves determining the layout, styles, and positioning of elements on the page.

### Display:
- The rendered content is displayed in the browser window, and the user sees the fully loaded webpage.

### Additional Resource Loading:
If the webpage contains asynchronous requests (e.g., AJAX requests), additional resources may be loaded dynamically after the initial page load.

## What is CSS
Cascading Style Sheets, is a style sheet language used for describing the presentation of a document written in HTML or XML. CSS defines how elements should be displayed on a webpage, including their layout, colors, fonts, spacing, and other visual properties.
## How to add style to an element
```css
p {
  color: red;
}
/* Selector: p, Property: color, Value: red */ 
```
## What is a class
class is specified using class attribute.
```html
<p class="paragraph"><p>
```
## What is a selector
A selector is a pattern or a set of rules that define which elements in an HTML document the styles should be applied to.
## How to compute CSS Specificity Value
### Priority
- 1, Inline Styles
- 2, ID Selectors
- 3, Class, Attribute, and Pseudo-class Selectors
- 4, Type and Pseudo-element Selectors(: p or ::first-line )
## What are Box properties in CSS
the "box properties" refer to a set of properties that define the visual properties and layout of an HTML element as a rectangular box.