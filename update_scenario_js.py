with open('gitoops/js/scenario.js', 'r') as f:
    content = f.read()

# Add a function to generate JSON-LD at the end of the file
json_ld_code = """
function injectJsonLd(scenario) {
  const schema = {
    "@context": "https://schema.org",
    "@type": "HowTo",
    "name": scenario.title,
    "description": scenario.description,
    "step": scenario.steps.map((step, index) => ({
      "@type": "HowToStep",
      "name": step.condition || `Step ${index + 1}`,
      "text": step.explanation,
      "itemListElement": [{
        "@type": "HowToDirection",
        "text": step.commands.join('\\n')
      }]
    }))
  };

  const script = document.createElement('script');
  script.type = 'application/ld+json';
  script.text = JSON.stringify(schema);
  document.head.appendChild(script);
}
"""
content += json_ld_code

# Call injectJsonLd inside renderScenario
content = content.replace(
    "setupCopyButtons();",
    "setupCopyButtons();\n  injectJsonLd(scenario);"
)

with open('gitoops/js/scenario.js', 'w') as f:
    f.write(content)
