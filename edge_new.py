import cv2


def edge_detector(path):
    # Input colored image
    colored_img = cv2.imread(path)

    # Exception handling
    assert colored_img is not None, "file could not be read, check with os.path.exists()"

    # Convert to grayscale
    gray_img = cv2.cvtColor(colored_img, cv2.COLOR_RGB2GRAY)

    # Find edges in grayscale image
    edges = cv2.Canny(gray_img, 100, 200)

    # Merge edges thrice to form 3 channel image
    # to add to the colored image
    three_edges = cv2.merge([edges, edges, edges])

    # Add weight - colored img and 3 channel edges
    processed_img = cv2.addWeighted(colored_img, 1, three_edges, 1, 0.0)

    # Save the processed image
    cv2.imwrite('processed.jpeg', processed_img)

    # Display before and after images

    # orig_img = cv2.resize(colored_img, (600, 400))
    # output_img = cv2.resize(processed_img, (600, 400))
    # cv2.imshow('original', orig_img)
    # cv2.imshow('processed', output_img)
    # cv2.moveWindow('processed', 600, 300)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Display processed image only

    # cv2.imshow('processed_img', processed_img)
    # cv2.moveWindow('processed', 600, 300)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Return processed image as function output
    return processed_img


# Call the function
edge_detector('khan.jpg')
