# Write a function that takes a concept title and 
# a concept description as input and then returns
# HTML that you can copy and paste into your notes 
# web page.

def build_content_panel(concept_title, concept_content):
    content_panel_template = '''
           <div class="standard_content panel">
                <h2 class="standard_content_title">{title}</h2>
                <p>
                {content}
                </p>
           </div>  
    '''
    content_panel = content_panel_template.format(title=concept_title, content=concept_content)
    return content_panel

title = "Random Concept Title"
content = '''HTML stands for <em>HyperText Markup Language</em>. HTML documents make up the 
                majority of the content on the web. HTML documents contain <em>text content</em> 
                which describes "what you see" and <em>markup</em> which describes "how it looks".'''

print build_content_panel(title, content)
