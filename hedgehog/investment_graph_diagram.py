from investment_graph import Start, investment_graph
import asyncio
import os


async def main():
    """Generate and save a mermaid diagram of the investment graph"""
    # Ensure an 'images' directory exists
    os.makedirs("images", exist_ok=True)

    # Get the mermaid code
    mermaid_code = investment_graph.mermaid_code(start_node=Start)

    # Print the mermaid code
    print("Mermaid diagram code generated:")
    print(mermaid_code)

    # Save the diagram as an image
    output_path = "images/investment_graph.png"
    try:
        await investment_graph.mermaid_save(output_path, start_node=Start)
        print(f"Diagram saved to {output_path}")
    except Exception as e:
        # If direct saving fails, provide instructions for manual generation
        print(f"Could not save diagram automatically: {e}")
        print("To generate manually:")
        print("1. Visit https://mermaid.live")
        print("2. Paste the mermaid code above")
        print("3. Export as PNG or SVG")


if __name__ == "__main__":
    asyncio.run(main())