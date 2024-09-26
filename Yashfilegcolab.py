{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOQpeMUCGIczODcGYwa+3Wz",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yashsgt/PythonCodes/blob/main/Yashfilegcolab.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "g69hYu4ERN0k"
      },
      "outputs": [],
      "source": [
        "h = 7 +8j"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "h.  real"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YQzxCib5RUXN",
        "outputId": "9ac26ba0-d73b-45df-e541-ad475daafac9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "7.0"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "h.imag"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S0S3Z7dmRYzZ",
        "outputId": "9673527d-225b-47e6-bc2c-43ba50478972"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "8.0"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "S1 = \"this is my string\""
      ],
      "metadata": {
        "id": "Bn8_SE-pRfKW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "type(S1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QJnjevMERk1m",
        "outputId": "64d78900-31a3-426d-a961-bee10a9fe647"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "S = 'sudh'"
      ],
      "metadata": {
        "id": "rzmWg9u0Roxr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "type(S)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IcP9NluTRsze",
        "outputId": "e372c532-4a0f-4adb-ba26-18a35e9314fc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "len(S)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G73CdgRhRxTD",
        "outputId": "97d5e2ff-81ff-4bf4-adcf-e3e51be131ea"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Use of x.find() ?\n",
        "s = 'sudh'"
      ],
      "metadata": {
        "id": "YaRGxXRtSopL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "s.find('h')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iCJwT-UwS0_P",
        "outputId": "0395d523-5d8d-4d36-b44e-9faa3b81b977"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s2=\"pwskills\""
      ],
      "metadata": {
        "id": "dsQDIkpXTBjZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "s2.find('l')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "muPf3zBXTJCo",
        "outputId": "6bc95594-2af9-4f0a-897e-fedf6d5f1845"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s2.find('sk')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lBnR6e3wTRXy",
        "outputId": "a4cda986-ae8a-4316-f86f-95524c82d3f0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s.find('S')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AMBw-H-9Tcjh",
        "outputId": "75329d73-d41d-41f1-e4d7-334395d14922"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "-1"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Count function;\n",
        "# to find the indexing of an unknown letter\n",
        "\n",
        "s = \"pwskills\""
      ],
      "metadata": {
        "id": "x_u6FMtNT0Xa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "s.count('z')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3IS9f9JXUI3p",
        "outputId": "8dddbd02-6531-4f5a-b2cd-5a7faf51b656"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Upper function and lower function;\n",
        "s2 = \"pwskills\""
      ],
      "metadata": {
        "id": "rVLWyaOKUPHj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "s2.upper()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "Cfptn3srUbCB",
        "outputId": "04eb7396-3531-4d1f-df41-4d43c958f04f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'PWSKILLS'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s2.lower()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "pa6FhIgZUv9i",
        "outputId": "95169b27-e070-4f93-84d6-aae1c486930f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'pwskills'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Use of swapcase function:-\n",
        "# by x.swapcase(), where x is any variable;\n",
        "\n",
        "s4=\"COMPetition\"\n",
        "s5=\"RAJputana\""
      ],
      "metadata": {
        "id": "uzBR8w1rVBv_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "s5.swapcase()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "b1L5Tn-gVlbO",
        "outputId": "22ac5116-de3c-4081-caec-19811a94f348"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'rajPUTANA'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s4.swapcase()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "_RxFx6OnVY5C",
        "outputId": "d5916684-1d19-4665-8ac3-21e42a689c26"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'compETITION'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Use of capitalize function.\n",
        "# s1.capitalize\n",
        "s1 = \"This IS My worLD\""
      ],
      "metadata": {
        "id": "i2Hj0q9VVsvq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "s1.capitalize()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "wqsugit9WeSN",
        "outputId": "d3730158-81f9-433a-b52f-db43d018eb61"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'This is my world'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# String Indexing and Slicing.\n",
        "s = \"physicswallah\"\n"
      ],
      "metadata": {
        "id": "9H_41dROWkqs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "s[5]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "3n4VuXGJXVwK",
        "outputId": "a170a0af-33f9-494c-d6f5-f3e11e59ed56"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'c'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s[-10]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "WDOQyHapXqfb",
        "outputId": "63ad48c6-a990-4373-c59b-fa3c266d9a07"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'s'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Slicing.\n",
        "\n",
        "s = \"pwskills\"\n",
        "\n",
        "s[0:5]\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "l-9jxqw6X9Pf",
        "outputId": "18469137-3c71-4126-9a9f-cdaffbc37fc3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'pwski'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s[4:7]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "C6-ulLxpYVYI",
        "outputId": "f958db01-bb7d-42b4-ed48-c5216afae35c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'ill'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 44
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# If we want alternate position of substring then it depends on 'jump or gap' you have taken....\n",
        "s[1:7:2]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "IIX6tLbrYmta",
        "outputId": "7b8246aa-b139-4ab3-dd70-1462a4c59e40"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'wkl'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s[2:6:3]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "XAuLhJ6GZNnZ",
        "outputId": "f987c649-6012-4ad3-829b-58744ce71f5f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'sl'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# During slicing no matter what is the range in [] and what is the range of our string, It will run as from 0 to ending point as per direction you opted.\n",
        "s[1:1000:2]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "zPsiSzERZd6Y",
        "outputId": "ce46e303-1e4c-4323-eb5a-f9b4fca7e857"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'wkls'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 47
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# special case;\n",
        "s= \"pwskills\"\n",
        "s[2:7:-1]\n",
        "# Due to direction conflict, we get a blank.\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "UAmPVA3TaBRP",
        "outputId": "091e9f83-f17c-4cb5-87d2-42e19d458d30"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "''"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 50
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s[7:2:-1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "rtzBSewBafxN",
        "outputId": "317394aa-5b78-4ec3-c246-7a254bbabcca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'sllik'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Special case:- If we want reversal of string.\n",
        "s=\"pwskills\"\n",
        "s[ : :-1]\n",
        "# That means starting from that end which makes you able to move in given direction."
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "AqLW1GkSarGt",
        "outputId": "69b7e1ed-19fe-4a20-eb9e-8a47e1bd4242"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'sllikswp'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s[7: :-1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "QYxI9dXDbB1l",
        "outputId": "c85a555a-7653-4bd3-f44f-0d41148a4c42"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'sllikswp'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 56
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s[7:0:-1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "FetFn_c4bfcI",
        "outputId": "16775e9e-8f46-4dc3-e4ff-6a189d9dae32"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'slliksw'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# LISTS ;\n",
        "L = []"
      ],
      "metadata": {
        "id": "xGAmr8i8b_IW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "type(L)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7b-v9dafcNGB",
        "outputId": "f8544213-7f9f-4287-edae-3d3025d2895e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "list"
            ]
          },
          "metadata": {},
          "execution_count": 60
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "l1 = [1,3,5,6,7,6,5,4,5]"
      ],
      "metadata": {
        "id": "99J0rG0wcWYL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "type(l1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_duOU1nncbyn",
        "outputId": "86ae8ff3-5b90-42b7-aa74-da036371c3c5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "list"
            ]
          },
          "metadata": {},
          "execution_count": 62
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "l1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ftbfjxXxcfCi",
        "outputId": "32d80f12-b8e5-4831-bcd8-e29113e9aed8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 3, 5, 6, 7, 6, 5, 4, 5]"
            ]
          },
          "metadata": {},
          "execution_count": 63
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "l2 = [1,2,3,4,5.6,\"Maharana pratap\",True,4+6j]"
      ],
      "metadata": {
        "id": "tQGmDFOJcnXA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "type(l2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1azKK-lZc2bO",
        "outputId": "031dc3b5-0773-4ed9-e49e-822e34e7a883"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "list"
            ]
          },
          "metadata": {},
          "execution_count": 65
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "l2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9xygJYo2c58S",
        "outputId": "e0489481-71a4-4df7-dc9a-0d44a305db0b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 2, 3, 4, 5.6, 'Maharana pratap', True, (4+6j)]"
            ]
          },
          "metadata": {},
          "execution_count": 66
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# If we want indexing or slicing from the list:-\n",
        "\n",
        "l3=[\"Yash Rajput\",5,43.65,True]"
      ],
      "metadata": {
        "id": "eDnQ5Uekc9u8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "l3[1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "49a61yhtdfph",
        "outputId": "68e08ff0-5267-47ba-88e2-02f8dea730ae"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5"
            ]
          },
          "metadata": {},
          "execution_count": 68
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "l3[3]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YZG1ON9hdoJU",
        "outputId": "e33ccf10-0797-4e23-f57b-14d82da0d1af"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 70
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Note during indexing range matters if it will go out range then error occurs.\n",
        "# But in case of slicing range doesn't matter if it will go out of range then, during slicing it will be print as upto maximum possible range according to the given direction.\n"
      ],
      "metadata": {
        "id": "peftNYEpeDHh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Indexing of Lists:-\n",
        "l3 = [\"sudh\",5,45.67,True]\n",
        "l3[2]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eZrEK8cRfLH3",
        "outputId": "6a6767b2-31af-40fe-83d2-9dc4838d4caf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "45.67"
            ]
          },
          "metadata": {},
          "execution_count": 73
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "l3[1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZQxfH1DTffVy",
        "outputId": "340c22ce-51b6-46ba-c987-f363edfa2b71"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5"
            ]
          },
          "metadata": {},
          "execution_count": 75
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Slicing of Lists:-\n",
        "l3 = ['sudh',5,45.67,False]\n",
        "l3[0:3:2]\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SLkxvXh1ftJ_",
        "outputId": "129218ad-c031-444e-dbcb-cec8a4525b88"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['sudh', 45.67]"
            ]
          },
          "metadata": {},
          "execution_count": 78
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "l3[0:3]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4p07wnUmgMqm",
        "outputId": "3a392803-9f9b-4655-8f6e-5fbcfbe751d3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['sudh', 5, 45.67]"
            ]
          },
          "metadata": {},
          "execution_count": 79
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Reversal of data:-\n",
        "l3[ : :-1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HCJnsUktgU_W",
        "outputId": "b635c5ed-c6c8-417e-9176-0072a21183fa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[False, 45.67, 5, 'sudh']"
            ]
          },
          "metadata": {},
          "execution_count": 80
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "l3[3: :-1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VXNbWdaRgz7w",
        "outputId": "43432ee8-ba54-4ad4-ce1b-9f184dc901c5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[False, 45.67, 5, 'sudh']"
            ]
          },
          "metadata": {},
          "execution_count": 82
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "l3[3:0:-1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ow5M8tu9gfNr",
        "outputId": "086cefc1-3a22-43f2-868a-a55264e7fa30"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[False, 45.67, 5]"
            ]
          },
          "metadata": {},
          "execution_count": 81
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# To change the data from the list :-\n",
        "l3 = ['sudh',5,45.67,False]\n",
        "l3[3]=100\n",
        "l3"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6X9_PHrXhZ74",
        "outputId": "617c9b79-c637-41e2-b419-4edb4d88219d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['sudh', 5, 45.67, 100]"
            ]
          },
          "metadata": {},
          "execution_count": 86
        }
      ]
    }
  ]
}